from Company import Company
from Department import Department
from Manager import Manager
from PartTimeEmployees import PartTimeEmployee
from FullTimeEmployee import FullTimeEmployee

def main():
    '''main function that contains department objects and add Employee objects into the departments with details.'''
    #Employees objects creation
    FT1 = FullTimeEmployee(101, 'Jeff', False, 3)
    FT2 = FullTimeEmployee(102, 'Jim', True, 4)
    PT1 = PartTimeEmployee(103, 'Joe', False, 20)
    FT3 = FullTimeEmployee(104, 'Jack', True, 2)
    FT4 = FullTimeEmployee(105, 'Jane', False, 1)
    M1 = Manager(106, 'Tom', False, 4)
    M2 = Manager(201, 'Neil', False, 4)
    FT5 = FullTimeEmployee(205, 'Charles', False, 4)
    PT2 = PartTimeEmployee(204, 'Darren', True, 32)
    FT6 = FullTimeEmployee(203, 'Elliot', False, 3)
    PT3 = PartTimeEmployee(202, 'Fred', True, 10)
    #Departments objects creation
    D1 = Department('IT Helpdesk', M1, True)
    D2 = Department('Marketing', M2, False)
    #add Employeees into IT Helpdesk Dept.
    D1.addEmployee(FT1)
    D1.addEmployee(FT2)
    D1.addEmployee(PT1)
    D1.addEmployee(FT3)
    D1.addEmployee(FT4)
    D1.addEmployee(M1)
    #add Employees into Marketing Dept.
    D2.addEmployee(M2)
    D2.addEmployee(FT5)
    D2.addEmployee(PT2)
    D2.addEmployee(FT6)
    D2.addEmployee(PT3)
    #Company object creation and adding Departments.
    C1 = Company('SUSS', 'EDU1002334')
    C1.addDepartment(D1)
    C1.addDepartment(D2)
    #invoke __str__ method  method of the company
    print(C1)
    #update _SAFE_MANAGEMENT_PERCENTAGE to 40, then invoke __str__  method
    Company.setSafeManagementPercentage(40)
    print(C1)
main()