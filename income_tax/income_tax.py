# -- coding: UTF-8 --

""" Construct classes which will allow you to calculate Income Tax for an Individual for a given year, age
residential status and his/her salary.
"""

__author__ = 'saranya@gyandata.com'


class Person:
    """
    A class to store the details of the person like age, residential status and salary

    :ivar year: The year in which the person has the following details
    :vartype year: str

    :ivar age: Age of the person
    :vartype age: int

    :ivar residential_status: Residential status of the person. If the person is resident, then his status is A,
                               if Non Resident, B and if Not Ordinary Resident C
    :vartype residential_status: str

    :ivar salary: Income of the person for the above mentioned year
    :vartype salary: int

    """
    def __init__(self, year, age, residential_status, salary):
        self.year = year
        self.age = age
        self.residential_status = residential_status
        self.salary = salary


class TaxParameters:
    """ A class to store the store the tax slab rates for a particular year.
    The equation to calculate tax can be written as:

    tax = (salary - x_offset) * tax_rate + constant
    health and educational cess = tax * he_cess
    tax liability = tax + health and educational cess

    :vartype tax_rate: float
    :vartype salary: int
    :vartype x_offset: int
    :vartype constant: int

    """
    def __init__(self, x_offset, tax_rate, cess, constant):
        self.tax_rate = tax_rate
        self.he_cess = cess
        self.constant = constant
        self.x_offset = x_offset


class CalculateMixin:
    """
    A class to calculate the tax liability
    """
    def calculate(self):
        tax = (self.salary - self.x_offset) * self.tax_rate + self.constant
        cess = self.he_cess * tax
        total_tax = tax + cess
        return total_tax


class CalculateTax(Person, TaxParameters, CalculateMixin):
    """ A class which inherits class Person, TaxParameters and class Calculate Mixin """
    def __init__(self, year, age, residential_status, salary, x_offset, tax_rate, cess, constant):
        super().__init__(year, age, residential_status, salary)
        self.x_offset = x_offset
        self.tax_rate = tax_rate
        self.he_cess = cess
        self.constant = constant
