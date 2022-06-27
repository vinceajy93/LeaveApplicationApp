
from Leave import LeaveApplicationException
from VaccinationLeave import VaccinationLeave, Leave, datetime
from Manager import Manager, FullTimeEmployee
from PartTimeEmployees import PartTimeEmployee
from Department import Department, Company

def menu():
    '''menu methods that prints the menu options out and returns choice by user after error checking.'''

    while True:
        print("\nMenu\n======")
        print("1. Apply Leave\n2. Cancel Leave\n3. Display Employee Leave Profile\n4. Daily Movement Update\n5. Update Safe Management Measure Percentage\n6. Display Departments' SMM status\n0. Exit")
        choice = input("Enter option: ")

        if choice in '1234560' and len(choice) == 1:
            return choice     
        else:
            print("\nInvalid Option!")

def main():
    '''main function that takes in user input then returns results based on the inputs, ending the programme when a break is detected.'''
    try:
        #Employees objects creation
        FT1 = FullTimeEmployee(101, 'Syah', False, 3)
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
        #add Employeees into Marketing Dept.
        D2.addEmployee(M2)
        D2.addEmployee(FT5)
        D2.addEmployee(PT2)
        D2.addEmployee(FT6)
        D2.addEmployee(PT3)
        #Company object creation and adding Departments.
        C1 = Company('SUSS', 'EDU1002334')
        C1.addDepartment(D1)
        C1.addDepartment(D2)
        #create leaves for employees
        L1 = Leave(FT1,datetime(2021,6,30), datetime(2021,7,5))
        L2 = Leave(FT1,datetime(2021,7,15), datetime(2021,7,19))
        L3 = Leave(PT1,datetime(2021,6,29), datetime(2021,7,6))
        VL1 = VaccinationLeave(PT3,datetime(2021,6,30), datetime(2021,6,30))
        L4 = Leave(FT4,datetime(2021,6,30), datetime(2021,7,5))
        L5 = Leave(FT4,datetime(2021,7,7), datetime(2021,7,22))
        VL2 = VaccinationLeave(M1,datetime(2021,6,30), datetime(2021,6,30))
        VL3 = VaccinationLeave(M1,datetime(2021,7,30), datetime(2021,7,30))
        L6 = Leave(M2,datetime(2021,6,30), datetime(2021,7,5))
        VL4 = VaccinationLeave(M2,datetime(2021,7,6), datetime(2021,7,6))
        L7 = Leave(FT5,datetime(2021,6,30), datetime(2021,7,5))
        VL5 = VaccinationLeave(FT5,datetime(2021,7,30), datetime(2021,7,30))
        L8 = Leave(PT2,datetime(2021,6,30), datetime(2021,7,5))
        L9 = Leave(PT2,datetime(2021,7,7), datetime(2021,7,15))
        L10 = Leave(FT6,datetime(2021,6,30), datetime(2021,7,5))
        L11 = Leave(FT6,datetime(2021,7,9), datetime(2021,7,13))
        L12 = Leave(PT3,datetime(2021,7,5), datetime(2021,7,8))
        L13 = Leave(PT3,datetime(2021,7,13), datetime(2021,7,13))
    except LeaveApplicationException as l:
        print(f"{l} \n")
    else:
        #add leaves into the company database
        leavesList = [L1,L2,L3,VL1,L4,L5,VL2,VL3,L6,VL4,L7,VL5,L8,L9,L10,L11,L12,L13]
        for i in leavesList:
            C1.addLeave(i)
    
    while True:
        choice = menu()
        print() #for formatting use 
        if choice == '1':#apply leave
            try:
                employeeId = int(input("Enter employee ID: "))
                employeeDept = input("Enter employee's department: ")
                dept = C1.searchDepartment(employeeDept)
                if dept == None:
                    raise LeaveApplicationException
                else:
                    employeeObj = dept.searchEmployee(employeeId)
                    if employeeObj == None:
                        raise LeaveApplicationException
            except ValueError:
                print(f"{employeeId} must be of integer value.")
            except LeaveApplicationException:
                if dept == None:
                    print("No matching department, please re-try")
                elif employeeObj == None:
                    print("No such employee, please re-try") 
            else:  
                while True:
                    try:
                        fromDate = input("Enter from-date in dd/mm/yyyy:")
                        fromDate = datetime.strptime(fromDate,"%d/%m/%Y")
                        break
                    except ValueError:
                        print(f"{fromDate} is not in the format dd/mm/yyyy")
                while True:
                    try:
                        toDate = input("Enter To-date in dd/mm/yyyy:")
                        toDate = datetime.strptime(toDate,"%d/%m/%Y")
                        break
                    except ValueError:
                        print(f"{toDate} is not in the format dd/mm/yyyy")
                while True:
                    isVacLeave = input("Vaccination leave? (Y/N): ").upper()
                    if isVacLeave not in 'YN' or len(isVacLeave) != 1:
                        print("Please enter only Y or N.")
                        continue 
                    break
                try:
                    if isVacLeave == 'Y':
                        #vaccincation leave
                        newLeave = VaccinationLeave(employeeObj,fromDate,toDate)
                        #check for 2 max vac leave per year
                        counts = C1.getVaccinationLeaveCount(employeeId, fromDate.year)
                        if counts <2:
                            C1.addLeave(newLeave)
                            print("Leave Request added!!")
                            print(newLeave)
                        else:
                            print("Not allow to apply more than 2 vaccination leaves within same year")
                    else:
                        #leave
                        newLeave = Leave(employeeObj,fromDate,toDate)
                        C1.addLeave(newLeave)
                        print("Leave Request added!!")
                        print(newLeave)
                except LeaveApplicationException as l:
                    print(l)     

        elif choice == '2': #Cancel Leave
            '''method validates user inputs for employeeID and leave request Id, then calls the method in the company class to cancel the leave request'''
            try:
                employeeId = int(input("Enter employee ID: "))
                leaveRequestID = int(input("Enter leave request ID to cancel: "))
                leavesList = C1.getLeave(employeeId)
                if len(leavesList) == 0: #leaves for this employee not found
                    print(f"Mo leave requests for this employee ID: {employeeId}")
                else:
                    leavesIDs = []
                    for leaves in leavesList:
                        #moves leaveRequestIDs of employee into a leavesIDs list, then check if leave is found.
                        if leaves.status == 'Approved':
                            leavesIDs.append(leaves.leaveRequestID)
                    if leaveRequestID in leavesIDs : #leave found, cancel the leave.
                        C1.cancelLeave(employeeId,leaveRequestID)
                        print(f"Leave request {leaveRequestID} cancelled successfully")
                    else:         
                        print(f"Leave request {leaveRequestID} not found for this employee.")
            except ValueError:
                print("Please insert only integers.")
        elif choice == '3': #Display Employee Leave Profile
            '''valid the employee ID and department name entered by user before displaying the employee details and all their leave requests.'''
            try:
                employeeID = int(input("Enter employee ID: "))
                employeeDept = input("Enter employee's department: ")
                dept = C1.searchDepartment(employeeDept)
                if dept == None: #department name not found
                    
                    print(f"Department {employeeDept} not found.")
                else:
                    employee = dept.searchEmployee(employeeID)
                    if employee == None: #employee not found
                        print(f"{dept.name} department has no employee with ID {employeeID}. Please re-try.")
                    else:
                        employeeLeaves = C1.getLeave(employeeID)
                        print()#formatting use
                        for leaves in employeeLeaves:
                            print(f"{leaves}\n")
            except ValueError:
                print("Please insert only numbers for employee ID.")
            except Exception as e:
                print(f"General unexcepted error: {e}")
           
        elif choice == '4': #Daily Movement Update
            '''validate employeeId and department name entered by the user before displaying current work from home status(True/False). Ask if the user want to change the status. if yes, toggle the workFromHome value for this employee.'''
            try:
                employeeID = int(input("Enter employee ID: "))
                employeeDept = input("Enter employee's department: ")
                dept = C1.searchDepartment(employeeDept)
                if dept == None: #department name not found
                    print(f"Department {employeeDept} not found.")
                else:
                    employee = dept.searchEmployee(employeeID)
                    if employee == None: #employee not found
                        print(f"{dept.name} department has no employee with ID {employeeID}.")
                    else:
                        print(f"Curent work from home status is {employee.workFromHome}")
                        newWFHStatus = input("Change the status? (Y/N): ").upper()
                        if newWFHStatus not in'YN' or len(newWFHStatus) != 1:
                            print("input not valid. please re-try.")
                        else:
                            if newWFHStatus == 'Y':
                                if employee.workFromHome == False:
                                    employee.workFromHome = True
                                else:
                                    employee.workFromHome = False
                                print(f"Work from home status for employee ID:{employeeID} has been changed to {employee.workFromHome}.")
            except ValueError:
                print("Please insert only numbers for employee ID.")
        elif choice == '5': #Update Safe Management Measure Percentage 
            '''this option displays current safe management measure % to the user, validate the user input for new % (0-100) then print out the adjusted % as confirmation.'''
            currentSMPercentage = C1.getSafeManagementPercentage()
            print(f"Current Safe Management Measure % is {currentSMPercentage:.1f}")
            try:
                newSMPercentage = float(input("Enter new Safe Management Measure %: "))
                
            except ValueError:
                print("Please insert only numbers")
            else:
                if 1<= newSMPercentage <=100:
                    #update SMM percentage to new percentage
                    C1.setSafeManagementPercentage(newSMPercentage)
                    currentSMPercentage = C1.getSafeManagementPercentage()
                    print(f"Safe Management Measure % updated to {currentSMPercentage}")
                else:
                    print("Sorry, please re-enter within range (0, 100)")

        elif choice == '6': #Display Departments' SMM status 
            '''this option prints out the current safe management measure status for all departments of the company.'''
            print(C1)
        else: #exit
            break
main()