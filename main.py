import webbrowser
import os
import templates
from datetime import date
from datetime import datetime
import time
from typing import List

# only videos in mp4 format

class App():
    def __init__(self) -> None:
        self.current_date = date.today().strftime('%d.%m.%Y')

    def open_web(self):
        'open overview todays birthdays in browser'
        webbrowser.open('file://' + os.path.realpath('birthday.html'))

    def read_file(self) -> List[list]:
        persons = []
        with open('input.csv', 'r') as file:
            for line in file:
                tmp = line.split(',')
                if ' \n' in tmp:
                    tmp.remove(' \n')
                if tmp[2] == self.current_date:
                    persons.append(tmp)
        return persons

    def validate_date(date:str):
        try:
            datetime.strptime(date, '%d.%m.%Y')
        except ValueError:
            raise ValueError('date should be formatted like dd.mm.yyyy')
        return True
  
    def validate_gender(gender:str):
        """checks if gender is one of the three allowed"""
        genders = ['m','w','n']
        if gender in genders:
            return True
        else:
            raise ValueError('gender should be m, w, or n')

    def validate_video(video:str):
        """checks if video has format mp4"""
        if video.endswith('.mp4'):
            return True
        else:
            raise ValueError('videos should have type mp4')

    def prepare(self, persons: List[list]) -> List[dict]:
        'prepare data for displaying'
        return_list = []
        for person in persons:
            tmp_dict = {}
            tmp_dict['firstname'] = person[1]
            tmp_dict['lastname'] = person[0]
            if self.validate_gender(person[3]):
                tmp_dict['gender'] = person[3]
            if self.validate_date(person[2]):
                tmp_dict['birthdate'] = person[2]

            if len(person) > 4:
                if person[4].endswith('.mp4'):
                    tmp_dict['video'] = person[4]
                else:
                    if self.validate_video(person[4]):
                        tmp_dict['image'] = person[4]
            if len(person) > 5:
                tmp_dict['video'] = person[5]
            
            return_list.append(tmp_dict)
        
        return return_list

    def generate_page(self, persons: List[dict]):
        'generate web page for displaying birthdays'
        title = 'Birthday'
        with open('birthday.html', 'w') as file:
            file.write(templates.top.format(title=title))
            # check if there is a birthday
            if persons:
                for person in persons:
                    file.write(templates.name.format(firstname=person['firstname'], lastname=person['lastname'], gender=person['gender']))
                    file.write(templates.birthdate.format(birthdate=person['birthdate']))
                    if 'image' in person:
                        file.write(templates.image.format(source=person['image']))
                    if 'video' in person:
                        file.write(templates.video.format(source=person['video']))
            else:
                file.write(templates.no_bd)
            file.write(templates.bottom)

    def run(self):
        # open page on startup, realoads later with js
        self.generate_page(self.prepare(self.read_file()))
        self.open_web()
        while True:
            tmp = date.today().strftime("%d.%m.%Y")
            if tmp != self.current_date:
                self.current_date = tmp
                # rerun on new date
                self.generate_page(self.prepare(self.read_file()))
                self.open_web()
            time.sleep(60)

if __name__ == '__main__':
    app = App()
    app.run()