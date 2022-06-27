from Employee import Employee
from datetime import datetime, timedelta

class LeaveApplicationException(Exception):
    '''class to catch the exceptions raised by the LeaveApplication class.'''
    pass

class Leave:
    _NEXT_ID = 202100001 #format: YYYY99999
    def __init__(self, applicant:Employee, fromDate:datetime, toDate:datetime):
        '''constructor that executes when an object is created, given the applicant, fromDate and toDate as parameters'''
        self._leaveRequestId = Leave._NEXT_ID
        self._applicant = applicant
        self._fromDate = fromDate
        self._toDate = toDate
        Leave._NEXT_ID +=1
        #error checks with LeaveApplicationException class.
        if self._fromDate > self._toDate:
            raise LeaveApplicationException(f"Cannot create leave for {self._applicant.name}, {self._fromDate.strftime('%d %b %Y')} has to be the same or before {self.toDate.strftime('%d %b %Y')}.")
        elif self._fromDate.weekday() >= 5:
            raise LeaveApplicationException(f"Cannot create leave because {self._fromDate.strftime('%d %b %Y')} falls on Saturday or Sunday.")
        else:
            #no date related errors raised.
            dates = (self._fromDate + timedelta(i + 1)for i in range((self._toDate - self._fromDate).days))
            self._duration = sum(1 for day in dates if day.weekday() < 5) #exclude weekends
            if self._duration > self._applicant.leaveBalance:
                raise LeaveApplicationException(f"{self.applicant.name} do not have enough leave balance for this request. Have: {self.applicant.leaveBalance}  Requires: {self.duration}")
            self._status = "Approved"

    
    @property
    def leaveRequestID(self):
        '''returns the ID of the leave request.'''
        return self._leaveRequestId

    @property
    def applicant(self):
        '''returns the applicant's employee class.'''
        return self._applicant

    @property
    def fromDate(self):
        '''returns the starting date of the requested leave.'''
        return self._fromDate

    @property
    def toDate(self):
        '''returns the till date of the requested leave.'''
        return self._toDate

    @property
    def duration(self):
        '''returns the duration of the leave excluding weekends.'''
        return self._duration

    @property
    def status(self):
        '''returns whether status of the leave whether its Approved or Cancelled.'''
        return self._status

    @status.setter
    def status(self, newStatus):
        '''Sets the new status for the requested leave.'''
        self._status = newStatus

    def __str__(self):
        '''string representation of a Leave object.'''
        fromdateString = self.fromDate.strftime("%d %b %Y")
        toDateString = self.toDate.strftime("%d %b %Y")
        return f"Leave Request ID: {self.leaveRequestID}\nID: {self.applicant.employeeId}\tName: {self.applicant.name}\nFrom: {fromdateString}  to  {toDateString}\nDuration: {self.duration} days\nStatus: {self.status}"