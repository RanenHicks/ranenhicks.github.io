from Task import Task

# Declaring variables, removing magic numbers
STORESTASK = 1

class TaskService:

    # Citation for self usage: (Gyanendra371, 2024)

    # (Erakshaya485, 2024), initializes the class.
    def __init__(self, addTask, deleteTask, updateTask, taskList, taskId, taskDate, taskDescription):
        if addTask == None:
            return
        
        self.TaskService(addTask, deleteTask, updateTask, taskList, taskId, taskDate, taskDescription)

    # Main task service function
    def TaskService(self, addTask, deleteTask, updateTask, taskList, taskId, taskDate, taskDescription):

        self.added = False
        self.deleted = False
        self.updated = False
        taskExists = False

        if len(taskList) >= STORESTASK:

            # Checks if an task already exists with input id.
            for incrementTaskList in taskList:
                if taskId == incrementTaskList.getTaskId():
                    taskExists = True
        
                else:
                    taskExists = False
        
        # Adding task
        if addTask == True:
            confirmationTask = self.addingTask(addTask, taskExists, taskId, taskDate, taskDescription)

            return confirmationTask

        # Deleting task
        if deleteTask == True:
            self.deletingTask(deleteTask, taskExists, taskList, taskId)

        # Updating task
        if updateTask == True:
            self.updatingTask(updateTask, taskExists, taskList, taskId, taskDate, taskDescription)
                


    # Adds an task
    def addingTask(self, addTask, taskExists, taskId, taskDate, taskDescription): 
        
        # (Kalra, 2023; Everythingtech, 2023), initializing new task
        newTask = Task(None, None, None, True)

        # (TonyA, 2013; Rollbar Editorial Team, 2023), adding task with error checking
        try:
            if (addTask == True) and (taskExists == False):
                newTask.Task(taskId, taskDate, taskDescription)
                if newTask.addedCorrectly == False:
                    self.added = False
                    return
                else:
                    self.added = True
                    return newTask
        
        # User incorrect id error check
            elif (addTask == True) and (taskExists == True):
                raise Exception
        except:
            self.added = False
            print("Task with input id has already been made, please use another id.")

        
    # Deletes a task.
    def deletingTask(self, deleteTask, taskExists, taskList, taskId): 
        
        # Variable to iterate through task list to find location of same task
        sameTaskId = 0
        # (TonyA, 2013; Rollbar Editorial Team, 2023), deleting task with error checking
        try:
            if (deleteTask == True) and (taskExists == True):
                for incrementTaskList in taskList:
                    if taskId == incrementTaskList.getTaskId():
                        taskDelete = taskList.pop(sameTaskId)
                        taskDelete.deleteTaskInfo()
                        taskDelete = None
                        self.deleted = True
                
                    # Adds one after if statment since the list can store at [0]
                    sameTaskId += 1

            # User inccorect id error check
            elif (deleteTask == True) and (taskExists == False):
                raise Exception
        except:
                self.deleted = False
                print("Task with input id does not exist, can not delete.")

    # Updates a task.
    def updatingTask(self, updateTask, taskExists, taskList, taskId, taskDate, taskDescription): 
        
        # Variable to iterate through task list to find location of same task
        sameTaskId = 0

        # (TonyA, 2013; Rollbar Editorial Team, 2023), deleting task with error checking
        try:
            if (updateTask == True) and (taskExists == True):
                for incrementTaskList in taskList:
                    if taskId == incrementTaskList.getTaskId():
                        taskUpdate = taskList.pop(sameTaskId)
                        taskUpdate.updateTaskInfo(taskDate, taskDescription)
                        self.updated = True
                
                    # Adds one after if statment since the list can store at [0]
                    sameTaskId += 1

            # User inccorect id error check
            elif (updateTask == True) and (taskExists == False):
                raise Exception
        except:
                self.updated = False
                print("Task with input id does not exist, can not update.")

        
