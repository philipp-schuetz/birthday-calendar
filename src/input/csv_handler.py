from src import custom_types as ct
from pathlib import Path
import utils
import datetime as dt


class CSVInput:
    def __init__(self, file: Path):
        self.file = file

    def get_person_list(self) -> list[ct.Person]:
        """return all persons which were born on the current date"""
        person_list = []

        image = None
        video = None

        for person in self.read_file():
            if len(person) > 4:
                if utils.is_video_name(person[4]):
                    video = Path(person[4])
                else:
                    if utils.is_image_name(person[4]):
                        image = Path(person[4])
                        break
            if len(person) > 5:
                video = person[5]

            tmp_person = ct.Person(firstname=person[0], lastname=person[1], gender=person[2],
                                   birthdate=dt.date.fromisoformat(person[3]), image=image, video=video)

            person_list.append(tmp_person)

        return person_list

    def read_file(self) -> list[list]:
        """read data from file, remove unnecessary characters and convert to 2d list"""
        persons = []
        with open(self.file, 'r', encoding='UTF-8') as file:
            for line in file:
                line = line.strip().strip(',')
                tmp = line.split(',')
                if utils.birthdate_today(dt.date.fromisoformat(tmp[3])):
                    persons.append(tmp)
        return persons
