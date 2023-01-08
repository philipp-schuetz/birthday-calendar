import webbrowser
import os
import templates
from datetime import date
from typing import List

# only videos in mp4 format


current_date = date.today().strftime("%d.%m.%Y")
current_date = '01.01.2000'
secs_per_day = 86400
persons = []

def open_web():
    'open overview todays birthdays in browser'
    webbrowser.open('file://' + os.path.realpath('birthday.html'))

def read_file() -> list:
    return_list = []
    with open('input.csv', 'r') as file:
        for line in file:
            tmp = line.split(',')
            if ' \n' in tmp:
                tmp.remove(' \n')
            if tmp[2] == current_date:
                return_list.append(tmp)
    return return_list

def validate_input():
    pass

def prepare(persons: List[list]) -> List[dict]:
    'prepare data for displaying'
    return_list = []
    for person in persons:
        tmp_dict = {}
        tmp_dict['firstname'] = person[1]
        tmp_dict['lastname'] = person[0]
        tmp_dict['gender'] = person[3]
        tmp_dict['birthdate'] = person[2]

        if len(person) > 4:
            if person[4].endswith('.mp4'):
                tmp_dict['video'] = person[4]
            else:
                tmp_dict['image'] = person[4]
        if len(person) > 5:
            tmp_dict['video'] = person[5]
        
        return_list.append(tmp_dict)
    
    return return_list

def generate_page(persons: List[dict]):
    'generate web page for displaying birthdays'
    title = 'Birthday'
    with open('birthday.html', 'w') as file:
        file.write(templates.top.format(title=title))
        for person in persons:
            file.write(templates.name.format(firstname=person['firstname'], lastname=person['lastname'], gender=person['gender']))
            file.write(templates.birthdate.format(birthdate=person['birthdate']))
            if 'image' in person:
                file.write(templates.image.format(source=person['image']))
            if 'video' in person:
                file.write(templates.video.format(source=person['video']))
        file.write(templates.bottom)



def run():
    persons = read_file()
    generate_page(prepare(persons))

    open_web()

if __name__ == '__main__':
    run()