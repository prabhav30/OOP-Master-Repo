
# Academic Integrity Statement
# filename: "practical.py"
# author: Prabhav Mayankkumar BHAGAT
# student id: 524555
# email: 524555@learning.eynesbury.edu
# date: 25/11/2026
#
# This is all my own work as per the Eynesbury College Academic Integrity Policy 


import abc 

class Employee(metaclass=abc.ABCMeta):

    def __init__(self, first_name, last_name, employee_id):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.base_salary = 0

    def set_base_salary(self, salary):
        self.base_salary = salary

    @abc.abstractmethod
    def get_salary(self):
        pass

    @abc.abstractmethod
    def get_staff_info(self):
        pass

    