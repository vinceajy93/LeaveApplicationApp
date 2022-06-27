from Employee import Employee

class PartTimeEmployee(Employee):
    _LEAVE_ENTITLEMENT = {15:5, 30:10, 31:12} 

    def __init__(self, employeeId:int, name:str, workFromHome:bool, hoursPerWeek:int):
        '''Constructor that executes when an PartTimeEmployee object is created, given the employeeId, name, workFromHome as parameters.'''
        super().__init__(employeeId, name, workFromHome)
        self._hoursPerWeek = hoursPerWeek
        self._leaveBalance = self.getLeaveEntitlement()
  
    def getLeaveEntitlement(self):
        '''The getLeaveEntitlement method computes and returns the starting leave balance for part time employees.'''
        for key in type(self)._LEAVE_ENTITLEMENT:
            if self._hoursPerWeek <= key:
                return type(self)._LEAVE_ENTITLEMENT[key]
        return type(self)._LEAVE_ENTITLEMENT.get(key)

    def __str__(self):
        '''string representation of a PartTimeEmployee object.'''
        return super().__str__() + f" \t Hours/Week: {self._hoursPerWeek}"