import datetime as dt
from config import config


def birthdate_today(birthdate: dt.date) -> bool:
    """return true if birthdate is today"""
    today = dt.date.today()
    if birthdate.day == today.day and birthdate.month == today.month:
        return True
    return False


def is_video_name(name: str) -> bool:
    for suffix in config.allowed_video_suffixes:
        if name.endswith(suffix):
            return True
    return False


def is_image_name(name: str) -> bool:
    for suffix in config.allowed_image_suffixes:
        if name.endswith(suffix):
            return True
    return False
