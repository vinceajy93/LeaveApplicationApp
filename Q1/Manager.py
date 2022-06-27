from FullTimeEmployee import FullTimeEmployee

class Manager(FullTimeEmployee):
    _LEAVE_ENTITLEMENT = 25

    def getLeaveEntitlement(self):
        '''method getLeaveEntitlement references the class variable _LEAVE_ENTITLEMENT to return the leave balance for managers.'''
        return type(self)._LEAVE_ENTITLEMENT