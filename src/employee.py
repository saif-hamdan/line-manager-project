
class Employee:
    def __init__(self,employeeID,name,designation,containerCode,isDesignationSupervisory=False,isAddTask=False):
        self.employeeID = employeeID
        self.name = name
        self.designation = designation
        self.containerCode = containerCode
        self.isDesignationSupervisory = isDesignationSupervisory
        self.isAddTask = isAddTask
        # self.manager:Employee= None
        
        # def set_manager(manager:Employee):
        #     self.manager = manager

