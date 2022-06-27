from PartTimeEmployees import PartTimeEmployee
from Manager import FullTimeEmployee, Manager

def main():
    '''main function of the Leave Application System that creates the employees data and prints out their data.'''
    #objects creation
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
    #objects printing
    employeeList = [FT1,FT2,PT1,FT3,FT4,M1,M2,FT5,PT2,FT6,PT3]
    for employeeData in employeeList:
        print(employeeData)
    print() #leave a spacing in between for easier reading
    for employeeData in employeeList:
        #toggle the Work-From-Home setting for each employee
        if employeeData.workFromHome == True:
            employeeData.workFromHome = False
        else:
            employeeData.workFromHome = True
        print(employeeData)


main()