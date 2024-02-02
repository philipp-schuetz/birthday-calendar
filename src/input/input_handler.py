"""modules receives an input method and a filename and returns input data if it exists"""
from src import custom_types as ct
from csv_input import CSVInput
from pathlib import Path

# TODO get configuration options from config file
file_type = 'csv'
input_file = Path('input.csv')


def get_person_list() -> list[ct.Person]:
    match file_type:
        case 'csv':
            csv = CSVInput(input_file)
            return csv.get_person_list()
