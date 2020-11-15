from datetime import datetime

def date_from_filename(file_name):
    datetime_str = file_name
    datetime_str = datetime_str.replace('.jpg', "")
    datetime_str = datetime_str.replace('thermo', "")
    datetime_object = datetime.strptime(datetime_str, '%d-%m-%Y_%H_%M_%S')

    print(datetime_object)

    return datetime_object