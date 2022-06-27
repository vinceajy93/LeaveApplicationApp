from Leave import Leave, datetime, Employee, LeaveApplicationException
class VaccinationLeave(Leave):
    _fromThisDateOnwards = datetime(2020, 12, 30) 
    def __init__(self, applicant:Employee, fromDate: datetime, toDate: datetime):
        '''constructor that executes when an object is created, given the applicant, fromDate and toDate as parameters'''
        super().__init__(applicant, fromDate, toDate)
        #checks for input errors
        if fromDate != toDate:
            raise LeaveApplicationException("The dates do not match!")
        elif fromDate < type(self)._fromThisDateOnwards:
            errorMsg = type(self)._fromThisDateOnwards.strftime("%d %b %Y")
            raise LeaveApplicationException(f"Cannot apply Vaccination leave before {errorMsg}!")
        elif self._fromDate.weekday() >= 5:
            raise LeaveApplicationException("Leave request should not have from-date on weekend.")
        else:
            #no exceptions raised
            self._duration = 0
            self._status = "Approved"

    def __str__(self):
        '''string representation of a VaccinationLeave object.'''
        fromdateString = self.fromDate.strftime("%d %b %Y")
        toDateString = self.toDate.strftime("%d %b %Y")
        return f"Leave Request ID: {self.leaveRequestID}\nID: {self.applicant.employeeId}\tName: {self.applicant.name}\nFrom: {fromdateString}  to  {toDateString}\nDuration: {self.duration} day (vaccination)\nStatus: {self.status}"
