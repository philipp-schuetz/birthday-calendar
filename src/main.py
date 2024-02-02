import input_handler
import output_handler

if __name__ == '__main__':
    while True:
        persons = input_handler.get_person_list()
        output_handler.start_output(persons)
