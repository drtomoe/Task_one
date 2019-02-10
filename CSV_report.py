import csv
import re
from datetime import datetime
import pycountry
import os.path


def open_input_and_write_new_list():

    # check if input file exist
    if not os.path.exists('./input.csv'):
        print('Input file missing')
        exit()

    try:    # open with utf-8
        new_list = open_input_and_do_newlist('utf-8')

    except UnicodeDecodeError:      # open as utf-16
        new_list = open_input_and_do_newlist('utf-16')

    finally:
        new_list.sort()

        # write new_list to file as utf-8
        with open('output.csv', 'w', newline='', encoding='utf-8') as new_file:
            csv_writer = csv.writer(new_file)

            for line in new_list:
                csv_writer.writerow(line)


def open_input_and_do_newlist(encoding):
    with open('input.csv', 'r', newline='', encoding=encoding) as csv_file:
        # we assume no quoting, standard delimiter, open as dictionary
        csv_reader = csv.DictReader(csv_file, fieldnames=('date', 'region', 'impression', 'CTR'))

        new_list = []
        for line in csv_reader:
            new_list.append(new_line(line))
        return new_list


def new_line(old_line):
    """normalize data in one line"""
    return [date_change(old_line['date']),
            country_code(old_line['region']),
            old_line['impression'],
            clicks(old_line['impression'], old_line['CTR'])]


def date_change(date):
    """change date format"""
    try:
        obj_date = datetime.strptime(date, "%m/%d/%Y")
        return datetime.strftime(obj_date, "%Y-%m-%d")
    except ValueError:
        return '2099-01-01'


def country_code(region):
    """found 3-numeric country-cod for region"""
    try:
        country2 = pycountry.subdivisions.lookup(region).country_code
        return pycountry.countries.lookup(country2).alpha_3
    except LookupError:
        return 'XXX'


def clicks(impress, ctr):
    """calculate numbers of clicks, impress x CTR%, rounded"""
    try:
        # extract float from string CTR
        percent = float(re.findall('\d+\.\d+', ctr)[0])
        return round(int(impress) * percent / 100)
    except Exception:   # IndexError or ValueError
        return '?'


if __name__ == '__main__':
    open_input_and_write_new_list()
