import datetime as dt
from pathlib import Path
from typing import Optional


class Person:
    def __init__(self, firstname: str, lastname: str, gender: str, birthdate: dt.date, image: Optional[Path] = None,
                 video: Optional[Path] = None) -> None:
        self.firstname = firstname
        self.lastname = lastname
        if len(gender) != 1 or gender not in ['m', 'f', 'n']:
            raise ValueError("gender must be one of the following: m, f, n")
        else:
            self.gender = gender.lower()
        self.birthdate = birthdate
        self.image = image
        self.video = video
