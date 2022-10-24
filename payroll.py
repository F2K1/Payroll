import csv
import copy
from clerk import Clerk
from manager import Manager
from contractor import Contractor


class Payroll:

    def __init__(self):
        self.employees = []
        self.payrolls = []
    
    def load_employees(self):
        with open('code\employee.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                if row['Role'] == 'clerk':
                    row = Clerk(row['ID'], row['Name'], row['Surname'], row['Role'], row['Pay'], row['Hours'], row['Bonus'])
                    self.employees.append(copy.copy(row))
                    # self.employees.append(row.emp_name)
                    # self.employees.append(row.emp_surname)
                    self.payrolls.append(str(row.salary(row.emp_hours)))
                elif row['Role'] == 'manager':
                    row = Manager(row['ID'], row['Name'], row['Surname'], row['Role'], row['Pay'], row['Hours'], row['Bonus'])
                    self.employees.append(copy.copy(row))
                    # self.employees.append(row.emp_name)
                    # self.employees.append(row.emp_surname)
                    self.payrolls.append(str(row.salary(row.emp_bonus)))
                else:
                    row = Contractor(row['ID'], row['Name'], row['Surname'], row['Role'], row['Pay'], row['Hours'], row['Bonus'])
                    self.employees.append(copy.copy(row))
                    # self.employees.append(row.emp_name)
                    # self.employees.append(row.emp_surname)
                    self.payrolls.append(str(row.salary(row.emp_hours)))

    def print_payroll(self):
        print("Employee ID  ||  Payroll\n------------------------")
        i = 0
        while i < len(self.employees):
            print(self.employees[i].emp_name + " " + self.employees[i].emp_surname + ": " + self.payrolls[i] + "$")
            i += 1

if __name__ == '__main__':
    payroll = Payroll()
    payroll.load_employees()
    payroll.print_payroll()
    

