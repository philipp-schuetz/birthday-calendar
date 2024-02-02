import datetime as dt


def birthdate_today(birthdate: dt.date) -> bool:
    """return true if birthdate is today"""
    today = dt.date.today()
    if birthdate.day == today.day and birthdate.month == today.month:
        return True
    return False


def is_video_name(name: str) -> bool:
    allowed_extensions = ['mp4']  # TODO get values from config
    for extension in allowed_extensions:
        if name.endswith(extension):
            return True
    return False


def is_image_name(name: str) -> bool:
    allowed_extensions = ['png', 'jpg', 'jpeg']  # TODO get values from config
    for extension in allowed_extensions:
        if name.endswith(extension):
            return True
    return False
