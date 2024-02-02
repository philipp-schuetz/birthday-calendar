import webbrowser
from pathlib import Path
import html_css
import html_templates
from src import custom_types as ct
import os


class HtmlOutput:
    def __init__(self, data: list[ct.Person]):
        self.data = data
        self.html_out_file = Path('birthday.html')

        css_path = Path('style.css')
        if not css_path.is_file():
            with open(css_path, 'w', encoding='UTF-8') as file:
                file.write(html_css.css)

    def open_web(self):
        """open overview today's birthdays in browser"""
        webbrowser.open('file://' + os.path.realpath(self.html_out_file))

    def generate_page(self):
        """generate web page for displaying birthdays"""
        title = 'Birthday'
        # write modified templates to html file
        with open(self.html_out_file, 'w', encoding='UTF-8') as file:
            file.write(html_templates.top.format(title=title))
            # check if there is a birthday
            if self.data:
                for person in self.data:
                    file.write(html_templates.person_open)
                    file.write(html_templates.name.format(firstname=person.get_firstname(),
                                                          lastname=person.get_lastname(),
                                                          gender=person.get_gender()))
                    file.write(html_templates.birthdate.format(birthdate=person.get_birthdate().strftime('%m.%d.%Y')))
                    if person.get_image():
                        file.write(html_templates.image.format(source=person.get_image()))
                    if person.get_video():
                        file.write(html_templates.video.format(source=person.get_video()))
                    file.write(html_templates.person_close)
            else:
                # write templates for the case that no birthday exists on the current date
                file.write(html_templates.person_open)
                file.write(html_templates.no_bd)
                file.write(html_templates.person_close)
            file.write(html_templates.bottom)
