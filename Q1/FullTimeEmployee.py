from Employee import Employee

class FullTimeEmployee(Employee):
    _LEAVE_ENTITLEMENT = {4:22, 3:20, 2:18, 1:16}

    def __init__(self, employeeId: int, name: str, workFromHome: bool, grade:int):
        '''Constructor that executes when an FullTimeEmployee object is created, given the employeeId, name, workFromHome as parameters.'''
        super().__init__(employeeId, name, workFromHome)
        self._grade = grade
        self._leaveBalance = self.getLeaveEntitlement()

    def getLeaveEntitlement(self):
        '''method getLeaveEntitlement computes and returns the starting leave balance for full time employees'''
        for key in type(self)._LEAVE_ENTITLEMENT:
            if self._grade == key:
                return type(self)._LEAVE_ENTITLEMENT[key]
        return type(self)._LEAVE_ENTITLEMENT[key]

    def __str__(self):
        '''string representation of a FullTimeEmployee object.'''
        return super().__str__() + f" \t Grade: {self._grade}"