Hello, my name is Ranen Hicks and this is my ePortfolio that (currently) contains courswork from my Computer Science Capstone at SNHU.

## Self-Assesment:



## Artifact 1: Software Design and Engineering

### Narrative:
<details>
<summary> Click to read </summary>
    My CS-320 artifact is an incomplete program that was split up into three different parts. These parts were the appointment, contact, and task services which tested my ability to create software tests. Before my enhancement, there was no UI, so all of the input that was given to the code had to be hard coded. Now, as of the time of writing this, I have created a placeholder main UI that allows users to add and delete appointments that also includes error checking.  

    This artifact was perfect for the Software Design/Engineering artifact requirements as I could re-write the program into my favorite coding language, Python. This was a great opportunity to review my knowledge, show my prowess, and touch up on Python, as I have not made much with it after my CS-340 course which was multiple months ago. Also, the original artifact included security features, which, if I could re-write in Python, would show that I am able to write secure code in another language. 

    Overall, when looking back at the first module assignment, I believe I have done a good job of working towards completing the 4th and 5th course objectives that I laid out with this artifact (CS 499 Module One, n.d.). I am using unit testing to show my security mindset, while also using my skills and outside resources to create a functional program that takes user input to create appointments, and in the future contacts and security (CS 499 Module One, n.d.). I don’t believe that this artifact can really make use, or cover any of the other course objectives, except for maybe the 2nd through the written communications of the narrative I am writing now (CS 499 Module One, n.d.). 

    One of the biggest things that I had to do when I first started re-writing the program in Python was to open the Python documentation in another tab. This was because I forgot, and needed more knowledge to complete this assignment, especially concerning the error checking and unit tests. Not to mention that I wanted to use other sources as little as possible, trying to figure out problems myself than looking up fixes from other people. I started by working on the files in this order, Appointment, AppointmentService, AppointmentTest, AppointmentServiceTest, and Driver. Other than re-learning basic Python, I also learned a lot about error checking in Python, primarily about exceptions and the unit tests throughout this coding process. 

    The Appointment file, other than the driver, gave me the most problems as I had to get used to coding in Python again. One thing that caught me off guard was the variable declaration, as Python takes care of the variable type by itself, which was something I had forgotten and felt like I was coding incorrectly at the beginning. The other problems started showing when I wrote the Driver file, for example, when I imported the Appointment and AppointmentService files, and tried to use the files to create their respective objects and got an error in return. Another example would be when I figured out that I wrote my exception statements incorrectly, just raising them instead of catching them within a try statement, causing the program to end abruptly when encountering an exception (TerryA, 2013). This was not the intended functionality, as I wanted my code to continue running after running into an error through user input. To fix these problems I used other sources than the Python documentation, in which I created a type of makeshift bibliography in APA to cite these sources. This was not the end of the errors as when I re-wrote the exceptions, I noticed that my AppointmentTest and AppointmentServiceTest files no longer functioned correctly, showing tests failing when encountering these exceptions. Luckily, I was able to figure out a solution to the problem relatively quickly by creating flag variables within the object that stored if an action was carried out correctly.  

    Once these files were done, the rest of the files were pretty much a cake walk. This was because most of the functionality between the files were basically the same, except the contact and task services needed an update function. This, however, is very similar to the delete function, but instead of deleting the old input, they would be rewritten with the new user input. Knowing this, I did not run into much trouble while coding and debugging these files except for the small errors I would make when creating the new code. After all of these files were done, I added the functionality to the driver and debugged them as a whole program, where I, once again, did not run into any major problems. After this was done, I uploaded it to this ePortfolio. 

**References** 

CS 499 Module One Assignment Template (n.d.) [Class document]. Southern New Hampshire University. https://learn.snhu.edu/content/enforced/1644210-CS-499-11095.202456-1/Course%20Documents/CS%20499%20Module%20One%20Assignment%20Template.docx?isCourseFile=true&ou=1644210   

TerryA. (2013, September 25). Make python code continue after exception. Stack Overflow. https://stackoverflow.com/a/18994347 
</details>

### Old:

<details>
    <summary> Updated </summary>

```python
import datetime

# Declaring variables, removing magic numbers
APPOINTMENTIDMAX = 10
APPOINTMENTDESCRIPTIONMAX = 50


class Appointment:

    # Citation for self usage: (Gyanendra371, 2024)

    # (Erakshaya485, 2024), initializing appointment object
    def __init__(self, newAppointmentId, newAppointmentDate, newAppointmentDescription, newAppointmentInstantce): 
        if newAppointmentInstantce == True:
            return
        
        self.Appointment(newAppointmentId, newAppointmentDate, newAppointmentDescription)

    def Appointment(self, newAppointmentId, newAppointmentDate, newAppointmentDescription):


        # (TonyA, 2013; Rollbar Editorial Team, 2023), appointment id being set, and error checking.
        try:
            if len(newAppointmentId) <= APPOINTMENTIDMAX:
                self.addedCorrectly = True
                self.appointmentId = newAppointmentId

            # Too Long of id
            elif len(newAppointmentId) > APPOINTMENTIDMAX:
                print("Appointment id is too long, please keep it to 10 characters or less.")
                raise Exception()
            
            # Null Id
            elif newAppointmentId == None:
                print("Appointment id is null, please enter an id.")
                raise Exception()
            
        except:
             self.addedCorrectly = False
             return self
        
        # Calls functions to set input other information.
        self.setAppointmentDate(newAppointmentDate)

        # Returns to stop adding function
        if self.addedCorrectly == False:
             return self

        self.setAppointmentDescription(newAppointmentDescription)
        return self



    # Setters and getters
    def getAppointmentId(self):
          return self.appointmentId
    
    def getAppointmentDate(self):
          return self.appointmentDate
    
    def setAppointmentDate(self, newAppointmentDate):

        # Gets the current time for later comparison.
        dateToday = datetime.date.today()
        
        # (TonyA, 2013; Rollbar Editorial Team, 2023), Sets appointment date if is valid.
        try:
            if newAppointmentDate > dateToday:
                self.appointmentDate = newAppointmentDate
            
            # Date in past
            elif newAppointmentDate < dateToday:
                print("Appointment date is before the current date, please enter a valid date.")
                raise Exception
            
            # Null date input
            elif newAppointmentDate == None:
                print("Appointment date is null, please enter a date.")
                raise Exception
        except:
             self.addedCorrectly = False # Flags incorrect data
                
            

    def getAppointmentDescription(self):
          return self.appointmentDescription
    
    def setAppointmentDescription(self, newAppointmentDescription):

        # (TonyA, 2013; Rollbar Editorial Team, 2023), Appointment description being set as well as error checking.
        try:
            if len(newAppointmentDescription) <= APPOINTMENTDESCRIPTIONMAX:
                self.appointmentDescription = newAppointmentDescription

            # Description too long
            elif len(newAppointmentDescription) > APPOINTMENTDESCRIPTIONMAX:
                print("Appointment description is too long, please keep it to 50 characters or less.")
                raise Exception
            
            # Null description input
            elif newAppointmentDescription.equals(None):
                print(("Appointment description is null, please enter an description."))
                raise Exception
        except:
            self.addedCorrectly = False # Flags incorrect data
    
    # Function deletes information stored within object
    def deleteAppointmentInfo(self):
          self.appointmentId = None
          self.appointmentDate = None
          self.appointmentDescription = None
```  
 </details>       
        
             

## Artifact 2: Algorithms and Datastructures
### Old:

### Updated:

## Artifact 3: Databases
### Old:

### Updated:
