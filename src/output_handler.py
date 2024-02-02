from html_output import HtmlOutput
import custom_types as ct
import datetime as dt
import time

# TODO get configuration options from config file
output_type = 'html'


def start_output(data: list[ct.Person]):
    """takes the person data and runs the configured output, return on new date"""
    match output_type:
        case 'html':
            today = dt.date.today()
            html = HtmlOutput(data)
            html.generate_page()
            html.open_web()
            while True:
                # check if the current date is a new date
                new = dt.date.today()
                if new != today:
                    return
                time.sleep(60)
