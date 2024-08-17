import unittest
from Task import Task
from TaskService import TaskService
import datetime

class TaskTests (unittest.TestCase):

    # Task Service add tests
    def testTaskServiceAddCorrect(self):
        
        # Initializing empty list for test
        checkTaskList = []

        # # (Kalra, 2023; Everythingtech, 2023), initializing and entering correct info into the Task service
        checkTaskServices = TaskService(None, None, None, None, None, None, None)
        checkTaskServices.TaskService(True, False, False, checkTaskList, "1", datetime.date(2025, 1, 1), "1")
        
        # Checks added variable to see if addition happened
        self.assertEqual(checkTaskServices.added, True)
    
    def testTaskServiceAddIdIncorrect(self):
        
        # Creating Task test list
        checkTaskList = []

        # (Kalra, 2023; Everythingtech, 2023), creates an existing Task and stores it
        checkTask = Task(None, None, None, True)
        checkTask.Task("1", datetime.date(2025, 1, 1), "1")
        checkTaskList.append(checkTask) 

        # Initializes Task services
        checkTaskServices = TaskService(None, None, None, checkTaskList, None, None, None)
        
        # Inputs incorrect addition information into Task services
        checkTaskServices.TaskService(True, False, False, checkTaskList, "1", datetime.date(2025, 1, 1), "1")
        
        # Checks added variable to see if addition happened
        self.assertFalse(checkTaskServices.added)

    
    # Delete tests
    def testTaskServiceDeleteCorrect(self):
        
        # Creating Task test list
        checkTaskList = []

        # (Kalra, 2023; Everythingtech, 2023), creates an existing Task and stores it
        checkTask = Task(None, None, None, True)
        checkTask.Task("1", datetime.date(2025, 1, 1), "1")
        checkTaskList.append(checkTask) 

        # Initializes Task services and inputs correct deletion information
        checkTaskServices = TaskService(None, None, None, checkTaskList, None, None, None)
        checkTaskServices.TaskService(False, True, False, checkTaskList, "1", datetime.date(2025, 1, 1), "1")
        
        # Checks added variable to see if deletion happened
        self.assertEqual(checkTaskServices.deleted, True)

    def testTaskServiceDeleteIdIncorrect(self):
        
        # Creating Task test list
        checkTaskList = []

        # (Kalra, 2023; Everythingtech, 2023), initializes Task services
        checkTaskServices = TaskService(None, None, None, checkTaskList, None, None, None)
        
        # Inputs incorrect deletion information and checks for non-deletion
        checkTaskServices.TaskService(False, True, False, checkTaskList, "2", None, None)
        self.assertFalse(checkTaskServices.deleted)


    # Update tests
    def testTaskServiceUpdateCorrect(self):
        
        # Creating Task test list
        checkTaskList = []

        # (Kalra, 2023; Everythingtech, 2023), creates an existing Task and stores it
        checkTask = Task(None, None, None, True)
        checkTask.Task("1", datetime.date(2025, 1, 1), "1")
        checkTaskList.append(checkTask) 

        # Initializes Task services and inputs correct deletion information
        checkTaskServices = TaskService(None, None, None, checkTaskList, None, None, None)
        checkTaskServices.TaskService(False, False, True, checkTaskList, "1", datetime.date (2026, 1, 1), "2")
        
        # Checks added variable to see if deletion happened
        self.assertEqual(checkTaskServices.updated, True)

    def testTaskServiceUpdateIdIncorrect(self):
        
        # Creating Task test list
        checkTaskList = []

        # (Kalra, 2023; Everythingtech, 2023), initializes Task services
        checkTaskServices = TaskService(None, None, None, checkTaskList, None, None, None)
        
        # Inputs incorrect update.
        checkTaskServices.TaskService(False, False, True, checkTaskList, "2", None, None)
        self.assertFalse(checkTaskServices.updated)

# Starts unit tests        
if __name__== '__main__':
    unittest.main()