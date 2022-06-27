from Employee import Employee
from Company import Company
class Department:

    def __init__(self, name:str, manager:Employee, essentialServices:bool):
        '''constructor that executes when a Department object is created. given the name, manager and essential services as parameters.'''
        self._name = name
        self._manager = manager
        self._essentialServices = essentialServices
        self._employees = []

    @property
    def name(self):
        '''returns the name of the department.'''
        return self._name

    @property
    def essentialServices(self):
        '''if this department is under essential services, return True, otherwise False.'''
        return self._essentialServices
    
    def searchEmployee(self, employeeId:int):
        '''searchEmployee method searches the employee list using given employeeId given as parameter. returns the employee object with the matching employeeId. return None otherwise.'''
        if employeeId == self._manager.employeeId:
                return self._manager
        for i in range(len(self._employees)):
            if employeeId == self._employees[i].employeeId:
                return self._employees[i]
        return None

    def addEmployee(self, newEmployee:Employee):
        '''Adds a new employee given as a parameter into the _employees list if this employee is not in the department. method returns True if the employee is sucessfully added into the list and false otherwise. Manager is not included in the list.'''
        result = self.searchEmployee(newEmployee.employeeId)
        if result == None and result != self._manager:
            self._employees.append(newEmployee)
            return True
        return False
    
    def safeManagementCheck(self, Percentage:float):
        '''safeManagementCheck method counts all employees who are working from home is greater or equal to the percentage of employee working from home(including the manager) and returns a string with a "passed requirement" display if percentage is greater or equal to the parameter "percentage", otherwise display "failed requirement". A department can be “exempted” from the above check if it is providing essential services.'''
        #counts and computes percentage of employee working from home.
        counts = sum(e.workFromHome == True for e in self._employees)
        #include the manager
        if self._manager.workFromHome == True:
            counts +=1
        calculatedPercentage = counts / (len(self._employees)+ 1) * 100
        #display
        text = f"No. of Employees working from home: {counts} ({calculatedPercentage:.1f}%)"
        if self.essentialServices == True:
            return text + "- exempted."
        elif calculatedPercentage >= Percentage:
            return text + "- passed requirement."
        else:
            return text + "- failed requirement."

    def __str__(self):
        '''string representation of a Department object.'''
        employeeDataText = ""
        #checks to turn True/False into Yes/No
        if self.essentialServices == True:
            isEssentialService = 'Yes'
        isEssentialService = 'No'
        if self._manager.workFromHome == True:
            wfhText = 'Yes'
        wfhText = 'No' 
        for employee in self._employees:
            if employee.workFromHome == True:
                wfhText = 'Yes'
            wfhText = 'No'
        
        #string formatting
        dept = f"Department: {self._name}   Essential Services: {isEssentialService}\n"
        manager = f"Manager ID: {self._manager.employeeId}   Name: {self._manager.name} \tLeave Balance: {self._manager.leaveBalance}   WFH: {wfhText}\tGrade: {self._manager._grade}\n"
        for employeeData in self._employees:
            employeeDataText += employeeData.__str__() + '\n'
        smcText = self.safeManagementCheck(Company.getSafeManagementPercentage()) + '\n'
        return dept + manager + employeeDataText + smcText


