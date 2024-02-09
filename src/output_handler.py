from html_output import HtmlOutput
from video_output import VideoOutput
import custom_types as ct
import datetime as dt
import time
from config import config

output_type = config.get_output_method()


def new_day(today: dt.date) -> bool:
    """check if the current date is a new date"""
    new = dt.date.today()
    if new != today:
        return True
    return False


def start_output(data: list[ct.Person]):
    """takes the person data and runs the configured output, return on new date"""
    today = dt.date.today()
    match output_type:
        case 'html':
            html = HtmlOutput(data)
            html.generate_page()
            html.open_web()
            while True:
                if new_day(today):
                    return
                time.sleep(60)
        case 'video':
            video = VideoOutput(data)
            video.start_video()
