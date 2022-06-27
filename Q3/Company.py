from datetime import datetime
from Leave import LeaveApplicationException


class Company:
    _SAFE_MANAGEMENT_PERCENTAGE = 50.0 #% of employees working from home.

    def __init__(self, name:str, uniqueEntityNumber:str):
        '''constructor that executes when a Company object is created. given the name, name and uniqueEntityNumber as parameters.'''
        self._name = name
        self._uniqueEntityNumber = uniqueEntityNumber
        self._departments = []
        self._leaveApplications = {}


    @classmethod
    def getSafeManagementPercentage(cls):
        '''Class method getSafeManagementPercentage returns the Safe Management Percentage. '''
        return cls._SAFE_MANAGEMENT_PERCENTAGE

    @classmethod
    def setSafeManagementPercentage(cls, newPercentage:float):
        '''Class method setSafeManagementPercentage sets the Safe Management Percentage. '''
        cls._SAFE_MANAGEMENT_PERCENTAGE = newPercentage

    def searchDepartment(self, name:str):
        '''searchDepartment method uses the name parameter to search through the list of departments and returns the Department object with the matching name. returns None if not found.'''
        for i in range(len(self._departments)):
            if name == self._departments[i].name:
                return self._departments[i]
        return None

    def addDepartment(self, newDepartment):
        '''addDepartment method has a Department object as parameter and adds it into the _departments list if its not present in the list. Method returns True if added sucessfully and False otherwise.'''
        result = self.searchDepartment(newDepartment.name)
        if result == None:
            self._departments.append(newDepartment)
            return True
        return False

    def getLeave(self, employeeId:int):
        '''returns a list of leave objects for the given employeeId. An empty list will be return if this employee has no leave request.'''
        if employeeId in self._leaveApplications:
            return self._leaveApplications.get(employeeId)
        else:
            self._leaveApplications[employeeId] = []
            return self._leaveApplications[employeeId]

    def addLeave(self, leave):
        '''check for any overlapping of dates with existing approved leaves, If overlap, the method raises LeaveApplicationException with error message. Otherwise, add new leave.'''
        employeeId = leave.applicant.employeeId
        if self.overlappingLeave(employeeId, leave.fromDate, leave.toDate) == True:
            raise LeaveApplicationException(f"Leave request should not overlap with approved leaves.")
        else:
            self.getLeave(employeeId).append(leave)
            leave.applicant._leaveBalance -= leave.duration
            if leave.fromDate == datetime.today() or leave.toDate == datetime.today():
                leave.applicant.workFromHome = True

    def cancelLeave(self, employeeId:int, leaveRequestId:int):
        '''searches the dictionary to retrieve the list of leave objects for the given employeeId. Raise LeaveApplicationException when 0 leaves detected. Removes approved leave object then set its status to "Cancelled", leave duration is then return to the employee.'''
        leaveList = self.getLeave(employeeId)
        if len(leaveList) == 0: #0 leaves
            raise LeaveApplicationException(f"There is no leaves applied by this employee!")
        for leaveObject in leaveList:#leaveRequestId
            if leaveRequestId == leaveObject.leaveRequestID:
                if leaveObject.status == 'Approved':
                    leaveObject.status = 'Cancelled'
                    leaveObject.applicant._leaveBalance += leaveObject.duration
                    return
        raise LeaveApplicationException(f"LeaveID {leaveRequestId} not found!")

    def overlappingLeave(self, employeeId:int, fromDate:datetime, toDate:datetime):
        '''searches the _leaveApplications for approved leave requests for the given employeeId. The method returns True if the fromDate and toDate have any overlapping with existing leave requests. Returns False otherwise.'''
        #searches _leaveApplications using employeeId
        if employeeId in self._leaveApplications:
            employeeLeavesList = self._leaveApplications.get(employeeId)
            for leaves in employeeLeavesList:
               #check for overlapping
               if leaves.status == 'Approved':
                    objectFromDate = leaves.fromDate
                    objectToDate = leaves.toDate
                    overlap = min(objectToDate - fromDate, toDate - objectFromDate).days + 1
                    if overlap > 0: #positive means overlap
                        return True
                    else:
                        return False
        return False

    def getVaccinationLeaveCount(self, employeeId:int, year:int):
        '''returns the number of approved vaccination leaves matching the employeeId for that year.'''
        count = 0
        leaveList = self.getLeave(employeeId)
        for leaveObject in leaveList:
            #checks for leave applied via vaccination
            if type(leaveObject).__name__ == 'VaccinationLeave':
                if  leaveObject.fromDate.year == year and leaveObject.status == 'Approved':
                    count +=1
        return count

    def __str__(self):
        '''string representation of a company object.'''
        deptDicttext = ""
        text = f"Company: {self._name}\t\tUEN:{self._uniqueEntityNumber}\n"  
        for deparmentData in self._departments:
            deptDicttext += deparmentData.__str__()
        return text + deptDicttext 