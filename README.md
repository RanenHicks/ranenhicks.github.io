Hello, my name is Ranen Hicks and this is my ePortfolio that (currently) contains courswork from my Computer Science Capstone at SNHU.

## Self-Assesment:



## Artifact 1: Software Design and Engineering

### Narrative:

<details>
<summary> check </summary>

```python

import unittest
from Task import Task
import datetime

class TaskTests (unittest.TestCase):

    # Test with all information correct
    def testTaskAllCorrect(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)
        checkTask.Task("1", datetime.date(2025, 1, 1), "1")
    
        # Checks Task information
        self.assertEqual(checkTask.getTaskId(), "1")
        self.assertEqual(checkTask.getTaskDate(), datetime.date(2025, 1, 1))
        self.assertEqual(checkTask.getTaskDescription(), "1")
        self.assertTrue(checkTask.addedCorrectly)


    # Task id tests
    def testTaskIdLong(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)

        # Checks if Task was not added
        self.assertFalse(checkTask.Task("11111111111", datetime.date(2025, 1, 1), "1").addedCorrectly)


    def testTaskIdNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)

        # Checks if Task was not added
        self.assertFalse(checkTask.Task(None, datetime.date(2025, 1, 1), "1").addedCorrectly)


    # Task date tests
    def testTaskDateBeforeCurrent(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)

        # Checks if Task was not added
        self.assertFalse(checkTask.Task("1", datetime.date(2023, 1, 1), "1").addedCorrectly)


    def testTaskDateNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)

        # Checks if Task was not added
        self.assertFalse(checkTask.Task("1", None, "1").addedCorrectly)


    # Task description test
    def testTaskDescriptionLong(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)

        # Checks for addition of Task
        self.assertFalse(checkTask.Task("1", datetime.date(2025, 1, 1), (51 * "1")).addedCorrectly)


    def testTaskDescriptionNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)

       # Checks for addition of Task
        self.assertFalse(checkTask.Task("1", datetime.date(2025, 1, 1), None).addedCorrectly)
 
        
# Calls the unit tests
if __name__== '__main__':
    unittest.main()
    ```
</details>
### [Old Artifact](Engineering.md)
        
             

## Artifact 2: Algorithms and Datastructures
### Old:

### Updated:

## Artifact 3: Databases
### Old:

### Updated:


## References Used to Make this ePortfolio:

