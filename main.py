# -- coding: UTF-8 --

"""
Main file for income tax calculation
"""

import logging
import logging.config
import argparse
import json

from income_tax.income_tax import CalculateTax

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'  # use os.join.path


def setup_logging(default_path=LOGGER_CONFIG_PATH):
    """
    Function Description: To setup logging using the json file
    :param default_path: Path of the configuration file
    :type default_path: str
        """
    with open(default_path, 'rt') as file:
        config = json.load(file)
    logging.config.dictConfig(config)


def arg_parse():
    """
    Function Description: To parse command line arguments
    :return: command line arguments passed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", help='Year', type=str)
    parser.add_argument("-a", help='Age', type=int)
    parser.add_argument("-r", help='Residential Status', type=str)
    parser.add_argument("-s", help='Salary', type=int)

    return parser.parse_args()


def main():
    """ Main function """
    setup_logging()
    args = arg_parse()

    inp_year = args.y
    inp_age = args.a
    inp_rs = args.r
    inp_salary = args.s

    with open("it_calc.json") as file:
        calculation_data = json.load(file)

    if inp_age < 60:
        age = "A"
    elif inp_age < 80:
        age = "B"
    else:
        age = "C"

    if inp_salary < 500000:
        salary = "A"
    elif inp_salary < 1000000:
        salary = "B"
    else:
        salary = "C"

    for data in calculation_data:
        if data['year'] == inp_year and data["age"] == age and data["salary"] == salary and \
                data["residential_status"] == inp_rs:
            x_offset = data["x_offset"]
            tax_rate = data["tax_rate"]
            constant = data["constant"]
            he_cess = data["he_cess"]

    obj = CalculateTax(inp_year, inp_age, inp_rs, inp_salary, x_offset, tax_rate, he_cess, constant)
    total_tax = obj.calculate()
    print(total_tax)


if __name__ == '__main__':
    main()
