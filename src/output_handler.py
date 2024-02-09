import cv2

from html_output import HtmlOutput
from video_output import VideoOutput
import custom_types as ct
import datetime as dt
import time
from config import config
import sys

output_type = config.get_output_method()


def new_day_or_end_reached(today: dt.date) -> bool:
    """check if the current date is a new date"""
    new = dt.date.today()
    if new != today:
        return True
    if dt.datetime.now().time() >= config.get_output_time()['end']:
        return True
    return False


def start_output(data: list[ct.Person]):
    """takes the person data and runs the configured output, return on new date"""
    if config.get_output_time()['start'] <= dt.datetime.now().time() <= config.get_output_time()['end']:
        today = dt.date.today()
        match output_type:
            case 'html':
                html = HtmlOutput(data)
                html.generate_page()
                html.open_web()
                while True:
                    if new_day_or_end_reached(today):
                        return
                    time.sleep(60)
            case 'video':
                video = VideoOutput(data)
                full_quit = False

                while True:
                    video.play_frame()
                    if cv2.waitKey(video.frame_delay) & 0xFF == ord('q'):
                        full_quit = True
                        break
                    if new_day_or_end_reached(today):
                        break
                video.stop_video()
                if full_quit:
                    sys.exit()
    time.sleep(1)
