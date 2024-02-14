import datetime as dt
from pathlib import Path
from typing import Optional
from config import config


class Person:
    def __init__(self, firstname: str, lastname: str, gender: str, birthdate: dt.date, image: Optional[Path] = None,
                 video: Optional[Path] = None) -> None:
        self.firstname = firstname
        self.lastname = lastname
        if len(gender) != 1 or gender not in ['m', 'f', 'n']:
            raise ValueError("gender must be one of the following: m, f, n")
        else:
            self.gender = gender
        self.birthdate = birthdate

        # if a file path was provided, check if the file exists
        if image is not None and not image.exists():
            raise ValueError(f'file {image} does not exist')
        self.image = image

        if video is not None and not video.exists():
            raise ValueError(f'file {video} does not exist')
        self.video = video

        if image is None:
            self.image = config.get_default_image()
        if video is None:
            self.video = config.get_default_video()

    def get_firstname(self) -> str:
        return self.firstname

    def get_lastname(self) -> str:
        return self.lastname

    def get_gender(self) -> str:
        return self.gender

    def get_birthdate(self) -> dt.date:
        return self.birthdate

    def get_image(self) -> Path | None:
        return self.image

    def get_video(self) -> Path | None:
        return self.video
