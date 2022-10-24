from employee import Employee


class Contractor(Employee):

    def __init__(self, id, name, surname, role, pay, hours, bonus):
        super().__init__(id, name, surname, role, pay, hours, bonus)

    def salary(self, hours):
        self.hours = int(hours)
        return int(self.emp_pay) * self.hours