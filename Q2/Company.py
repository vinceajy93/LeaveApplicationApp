
class Company:
    _SAFE_MANAGEMENT_PERCENTAGE = 50.0 #% of employees working from home.

    def __init__(self, name:str, uniqueEntityNumber:str):
        '''constructor that executes when a Company object is created. given the name, name and uniqueEntityNumber as parameters.'''
        self._name = name
        self._uniqueEntityNumber = uniqueEntityNumber
        self._departments = []

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

    def __str__(self):
        '''string representation of a company object.'''
        deptDicttext = ""
        text = f"Company: {self._name}\t\tUEN:{self._uniqueEntityNumber}\n"  
        for deparmentData in self._departments:
            deptDicttext += deparmentData.__str__()
        return text + deptDicttext 