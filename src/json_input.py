import custom_types as ct
from pathlib import Path
import utils
import datetime as dt
import json


class JsonInput:
    def __init__(self, file: Path):
        self.file = file

    def get_person_list(self) -> list[ct.Person]:
        """return all persons which were born on the current date"""
        person_list = []

        with open(self.file, 'r', encoding='UTF-8') as file:
            persons = json.load(file)

            for person in persons:
                firstname = person['firstname']
                lastname = person['lastname']
                gender = person['gender']
                birthdate = dt.date.fromisoformat(person['birthdate'])
                image = None
                if 'image' in person:
                    image = Path(person['image'])
                video = None
                if 'video' in person:
                    video = Path(person['video'])
                if utils.birthdate_today(birthdate):
                    person_list.append(
                        ct.Person(firstname=firstname, lastname=lastname, gender=gender,
                                  birthdate=birthdate, image=image,
                                  video=video))

        return person_list
