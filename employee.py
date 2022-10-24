from abc import ABC, abstractmethod


class Employee:

    def __init__(self, id, name, surname, role, pay, hours, bonus):
        self.emp_id = id
        self.emp_name = name
        self.emp_surname = surname
        self.emp_role = role
        self.emp_pay = pay
        self.emp_hours = hours
        self.emp_bonus = bonus
    
    @abstractmethod
    def salary_calc(ABC):
        pass
    