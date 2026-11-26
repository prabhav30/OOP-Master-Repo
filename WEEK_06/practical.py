
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


class TeachingStaff(Employee):

    def __init__(self, first_name, last_name, employee_id,
                 teaching_area, category):
        super().__init__(first_name, last_name, employee_id)
        self.teaching_area = teaching_area

        if category >= 1 and category <= 5:
            self.category = category
        else:
            print("Error: The category of a teaching staff "
                  "should be between 1 and 5.")
            self.category = 1

    def get_salary(self):
        return self.base_salary

    def get_staff_info(self):
        return ('First name: ' + self.first_name +
                '\nLast name: ' + self.last_name +
                '\nEmployee ID: ' + str(self.employee_id) +
                '\nTeaching area: ' + self.teaching_area +
                '\nCategory: ' + str(self.category) +
                '\nSalary: ' + str(self.get_salary()))


class PaidEmployee(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_salary(self):
        pass

    @abc.abstractmethod
    def get_staff_info(self):
        pass

# Employee = PaidEmployee()

teacher = TeachingStaff("John", "Smith", 101,
                        "Mathematics", 2)
teacher.set_base_salary(50000)

print(teacher.get_salary())

class Person:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def print_person_details(self):
        return ('First name: ' + self.first_name +
                '\nLast name: ' + self.last_name +
                '\nDOB: ' + str(self.date_of_birth))


class Worker:
    def __init__(self, tax_file_number, super_number):
        self.tax_file_number = tax_file_number
        self.super_number = super_number

    def get_info(self):
        return ('Tax File Number: ' + str(self.tax_file_number) +
                '\nSuper Number: ' + str(self.super_number))