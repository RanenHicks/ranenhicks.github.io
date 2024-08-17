import datetime

# Declaring variables, removing magic numbers
TASKIDMAX = 10
TASKDESCRIPTIONMAX = 50


class Task:

    # Citation for self usage: (Gyanendra371, 2024)

    # (Erakshaya485, 2024), initializing task object
    def __init__(self, newTaskId, newTaskDate, newTaskDescription, newTaskInstantce): 
        if newTaskInstantce == True:
            return
        
        self.Task(newTaskId, newTaskDate, newTaskDescription)

    def Task(self, newTaskId, newTaskDate, newTaskDescription):


        # (TonyA, 2013; Rollbar Editorial Team, 2023), task id being set, and error checking.
        try:
            if len(newTaskId) <= TASKIDMAX:
                self.addedCorrectly = True
                self.taskId = newTaskId

            # Too Long of id
            elif len(newTaskId) > TASKIDMAX:
                print("Task id is too long, please keep it to 10 characters or less.")
                raise Exception
            
            # Null Id
            elif newTaskId == None:
                print("Task id is null, please enter an id.")
                raise Exception
            
        except:
             self.addedCorrectly = False
             return self
        
        # Calls functions to set input other information.
        self.setTaskDate(newTaskDate)
        self.setTaskDescription(newTaskDescription)

        # Returns object
        return self



    # Setters and getters
    def getTaskId(self):
          return self.taskId
    
    def getTaskDate(self):
          return self.taskDate
    
    def setTaskDate(self, newTaskDate):

        # Gets the current time for later comparison.
        dateToday = datetime.date.today()
        
        # (TonyA, 2013; Rollbar Editorial Team, 2023), Sets task date if is valid.
        try:
            if newTaskDate > dateToday:
                self.taskDate = newTaskDate
            
            # Date in past
            elif newTaskDate < dateToday:
                print("Task date is before the current date, please enter a valid date.")
                raise Exception
            
            # Null date input
            elif newTaskDate == None:
                print("Task date is null, please enter a date.")
                raise Exception
        except:
             self.addedCorrectly = False # Flags incorrect data
                
            

    def getTaskDescription(self):
          return self.taskDescription
    
    def setTaskDescription(self, newTaskDescription):

        # (TonyA, 2013; Rollbar Editorial Team, 2023), task description being set as well as error checking.
        try:
            if len(newTaskDescription) <= TASKDESCRIPTIONMAX:
                self.taskDescription = newTaskDescription

            # Description too long
            elif len(newTaskDescription) > TASKDESCRIPTIONMAX:
                print("Task description is too long, please keep it to 50 characters or less.")
                raise Exception
            
            # Null description input
            elif newTaskDescription.equals(None):
                print(("Task description is null, please enter an description."))
                raise Exception
        except:
            self.addedCorrectly = False # Flags incorrect data
    
    # Function deletes information stored within object
    def deleteTaskInfo(self):
          self.taskId = None
          self.taskDate = None
          self.taskDescription = None
    
    # Function updates information within object.
    def updateTaskInfo(self, newTaskDate, newTaskDescription):
        self.taskDate = self.setTaskDate(newTaskDate)
        self.taskDescription = self.setTaskDescription(newTaskDescription)
        
        
             