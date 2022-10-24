from employee import Employee


class Manager(Employee):

    def __init__(self, id, name, surname, role, pay, hours, bonus):
        super().__init__(id, name, surname, role, pay, hours, bonus)
    
    def salary(self, bonus):
        self.bonus = int(bonus)
        return int(self.emp_pay) + self.bonus 