from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employeeId:int, name:str, workFromHome:bool):
        '''Constructor that executes when an Employee object is created, given the employeeId, name and workFromHome as parameters.'''
        self._Id = employeeId
        self._name = name
        self._workFromHome = workFromHome
        self._leaveBalance = 0

    @property
    def employeeId(self):
        '''returns the ID of the employee. '''
        return self._Id

    @property
    def name(self):
        '''returns the name of the employee.'''
        return self._name
    
    @property
    def leaveBalance(self):
        '''returns the remaining leave balance of the employee.'''
        return self._leaveBalance

    @property
    def workFromHome(self):
        '''returns the work from home status of the employee.'''
        return self._workFromHome
    
    @workFromHome.setter
    def workFromHome(self, atHome:bool):
        '''sets the new work from home status for the employee.'''
        self._workFromHome = atHome
    
    @abstractmethod
    def getLeaveEntitlement(self):
        '''abstract method getLeaveEntitlement() for child classes to implement.'''
        pass

    def adjustLeave(self, adjustment:int):
        '''method adjusts the leaves by taking in a new leave parameter and adds it to current leaves avaliable.'''
        self._leaveBalance += adjustment

    def __str__(self):
        '''string representation of a Employee object.'''
        if self._workFromHome == True:
            text = 'Yes'
        else:
            text = 'No'
        return f"ID: {self._Id} \tName: {self._name} \tLeave Balance: {self._leaveBalance} \tWFH: {text}"
