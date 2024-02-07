from pathlib import Path
import custom_types as ct
import os
from config import config
import cv2


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

            text_pos = [20, 20]
            font_scale = 1
            spacing = 25
            text_color = (255, 255, 255)
            thickness = 2
            for person in self.data:
                text_pos[1] += spacing * font_scale
                if config.get_lastname_only():
                    text = f'{config.get_address_terms()[person.get_gender()]} {person.get_lastname()}'
                else:
                    text = f'{person.get_firstname()} {person.get_lastname()}'
                cv2.putText(
                    frame, text, text_pos, cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, thickness, cv2.LINE_AA)

            cv2.imshow('video', frame)

            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()
