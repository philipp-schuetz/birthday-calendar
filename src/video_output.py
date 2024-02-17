import custom_types as ct
from config import config
import cv2


class VideoOutput:
    def __init__(self, data: list[ct.Person]):
        self.data = data
        self.video_file = config.get_default_video()

        self.cap = cv2.VideoCapture(str(self.video_file))
        self.cv2_video = cv2.VideoCapture(self.video_file.name)

        self.fps = self.cv2_video.get(cv2.CAP_PROP_FPS)
        self.frame_delay = int(1000 / self.fps)

        cv2.namedWindow('video', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    def add_names(self, frame):
        text_start_pos = config.get_video_output_text_start_pos().copy()
        font_scale = config.get_video_output_font_scale()
        spacing_y = config.get_video_output_text_spacing_y()
        text_color = config.get_video_output_text_color()
        thickness = config.get_video_output_text_thickness()

        if self.data:
            for person in self.data:
                text_start_pos[1] += spacing_y
                if config.get_lastname_only():
                    text = f'{config.get_address_terms()[person.get_gender()]} {person.get_lastname()}'
                else:
                    text = f'{person.get_firstname()} {person.get_lastname()}'
                cv2.putText(
                    frame, text, text_start_pos, cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, thickness,
                    cv2.LINE_AA)
        else:
            cv2.putText(
                frame, config.get_no_birthday_text(), text_start_pos, cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color,
                thickness, cv2.LINE_AA)

    def play_frame(self):
        ret, frame = self.cv2_video.read()
        self.add_names(frame)

        if not ret:
            self.cv2_video = cv2.VideoCapture(self.video_file.name)
            return

        cv2.imshow('video', frame)

    def stop_video(self):
        self.cv2_video.release()
        cv2.destroyAllWindows()
