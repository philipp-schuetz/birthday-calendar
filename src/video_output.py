import webbrowser
from pathlib import Path
import html_css
import html_templates
import custom_types as ct
import os
from config import config
import cv2


class VideoOutput:
    def __init__(self, data: list[ct.Person]):
        self.data = data
        self.video_file = config.get_default_video()

        self.cap = cv2.VideoCapture(str(self.video_file))

    def add_text_overlay(self, frame, text, position=(50, 50), font_scale=1, font_thickness=2,
                         text_color=(255, 255, 255)):
        cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, font_thickness)

    def start_video(self):
        video = cv2.VideoCapture('test.mp4')

        fps = video.get(cv2.CAP_PROP_FPS)

        delay = int(1000 / fps)

        cv2.namedWindow('video', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        while True:
            ret, frame = video.read()

            if not ret:
                video = cv2.VideoCapture('test.mp4')
                continue

            cv2.putText(frame, 'Text', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.imshow('video', frame)

            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()
