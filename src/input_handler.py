"""modules receives an input method and a filename and returns input data if it exists"""
import custom_types as ct
from csv_input import CSVInput
from json_input import JsonInput
from config import config

input_file = config.get_input_file()


def get_person_list() -> list[ct.Person]:
    match input_file.suffix:
        case '.csv':
            csv = CSVInput(input_file)
            return csv.get_person_list()
        case '.json':
            json = JsonInput(input_file)
            return json.get_person_list()
