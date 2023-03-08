from src.employee import Employee
from typing import List



class Container:
    def __init__(self,containerCode,containerName=None):
        self.containerCode = containerCode
        self.parentContainer : Container = None
        self.childContainers:List[Container] = []
        self.employees:List[Employee] =[]
        self.manager: Employee = None
        self.containerName = containerName

    def addEmployee (self,employee):
        self.employees.append(employee)
        
    def addContainerName(self,containerName):
        self.containerName = containerName


    def addChildContainers(self,container):
        flag = True
       
        for con in self.childContainers:
            if con.containerCode == container.containerCode:
              
                flag = False
                
    
        if flag : 
            self.childContainers.append(container)
      
        
        
    def linkParentContainer(self,isParentContainerExists,parentContainer) :
        if isParentContainerExists:
            self.parentContainer = parentContainer
        else:
            newParent = Container(parentContainer)
            self.parentContainer = newParent
            newParent.addChildContainers(self)
            return newParent
        
        
    def whoIsManager(self):
        manager = None
        flag = True

        for employee in self.employees:
            if employee.isAddTask and employee.isDesignationSupervisory:
                manager = employee
                flag = False
                break
            
            if not employee.isAddTask and employee.isDesignationSupervisory:
                manager = employee
                flag = False

        if flag and self.parentContainer  is not None and self.parentContainer.manager is None: 
            self.parentContainer.whoIsManager()
            manager = self.parentContainer.manager
        elif flag and  self.parentContainer  is not None:
            manager = self.parentContainer.manager
        
            
        self.manager = manager
        


