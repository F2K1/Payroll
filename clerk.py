from employee import Employee


class Clerk(Employee):

    def __init__(self, id, name, surname, role, pay, hours, bonus):
        super().__init__(id, name, surname, role, pay, hours, bonus)

    def salary(self, hours):
        self.hours = int(hours)
        overtime = int(self.emp_pay) / 20 / 8
        return int(self.emp_pay) + self.hours * round(overtime)