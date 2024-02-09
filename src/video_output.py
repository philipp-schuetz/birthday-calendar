import custom_types as ct
from config import config
import cv2
import sys


class VideoOutput:
    def __init__(self, data: list[ct.Person]):
        self.data = data
        self.video_file = config.get_default_video()

        self.cap = cv2.VideoCapture(str(self.video_file))

    def start_video(self):
        video = cv2.VideoCapture(self.video_file.name)

        fps = video.get(cv2.CAP_PROP_FPS)

        delay = int(1000 / fps)

        cv2.namedWindow('video', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        while True:
            ret, frame = video.read()

            if not ret:
                video = cv2.VideoCapture(self.video_file.name)
                continue

            text_start_pos = config.get_video_output_text_start_pos()
            font_scale = config.get_video_output_font_scale()
            spacing_y = config.get_video_output_text_spacing_y()
            text_color = config.get_video_output_text_color()
            thickness = config.get_video_output_text_thickness()
            for person in self.data:
                text_start_pos[1] += spacing_y
                if config.get_lastname_only():
                    text = f'{config.get_address_terms()[person.get_gender()]} {person.get_lastname()}'
                else:
                    text = f'{person.get_firstname()} {person.get_lastname()}'
                cv2.putText(
                    frame, text, text_start_pos, cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, thickness,
                    cv2.LINE_AA)

            cv2.imshow('video', frame)

            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()
