"""holds the default configuration and methods to interact with the config file"""
import json
from pathlib import Path


class Config:
    """Config holds default contents for config.json and methods to apply the config"""

    def __init__(self) -> None:
        # path to config file
        self.path = Path('config.json')

        self.valid_output_method = ['html', 'video']
        self.allowed_image_suffixes = ['.png', '.jpg', '.jpeg']
        self.allowed_video_suffixes = ['.mp4']

        # default configuration
        self.default = {
            "input_file": "input.json",
            "output_method": "html",
            "lastname_only": False,
            "address_terms": {
                "m": "Mr.",
                "f": "Ms.",
                "n": "Mx."
            },
            "default": {
                "image": "example.png",
                "video": "example.mp4"
            },
            "video_output": {  # TODO text size and position?
                "text_color": "white",
            }
        }

        # holds config loaded from file
        self.config = {}

        # create config file with default values, if it does not exist
        self.create_file()
        self.load()

    def create_file(self):
        """create config file if it not already exists"""
        if not self.path.is_file():
            with open(self.path, 'w', encoding='UTF-8') as file:
                json.dump(self.default, file)

    def load(self):
        """load config dictionary from file"""
        with open(self.path, 'r', encoding='UTF-8') as file:
            self.config = json.load(file)
            for key in self.default.keys():
                if key not in self.config.keys():
                    raise ValueError(f'Key {key} not found in config file')

    def save(self):
        """save config dictionary to file"""
        with open(self.path, 'w', encoding='UTF-8') as file:
            json.dump(self.config, file)

    def get_input_file(self) -> Path:
        value = self.config['input_file']
        if not isinstance(value, str) or not Path(value).is_file():
            raise ValueError(f'{value} is not a valid input file')
        return Path(value)

    def get_output_method(self) -> str:
        value = self.config['output_method']
        if value not in self.valid_output_method:
            raise ValueError(f'{value} is not a valid output method')
        return value

    def get_lastname_only(self) -> bool:
        value = self.config['lastname_only']
        if not isinstance(value, bool):
            raise ValueError(f'lastname_only value is not a boolean')
        return value

    def get_address_terms(self) -> dict[str, str]:
        value = self.config['address_terms']
        for key, val in value.items():
            if not isinstance(val, str):
                raise ValueError(f'address terms must be a strings')
            if key not in ['m', 'f', 'n']:
                raise ValueError(f'address terms can only contain m/f/n')
        return value

    def get_default_image(self) -> Path:
        value = self.config['default']['image']
        if not isinstance(value, str) or not Path(value).is_file():
            raise ValueError(f'{value} is not a valid default image file')
        return Path(value)

    def get_default_video(self) -> Path:
        value = self.config['default']['video']
        if not isinstance(value, str) or not Path(value).is_file():
            raise ValueError(f'{value} is not a valid default video file')
        return Path(value)

    def get_video_output_text_colors(self) -> str:
        value = self.config['video_output']['text_color']
        allowed_colors = ['red', 'green', 'blue', 'white']
        if not isinstance(value, str) or value not in allowed_colors:
            raise ValueError(f'{value} color')
        return value


config = Config()