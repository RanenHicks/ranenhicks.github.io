Hello, my name is Ranen Hicks and this is my ePortfolio that (currently) contains courswork from my Computer Science Capstone at SNHU.

## Self-Assesment:



## Artifact 1: Software Design and Engineering
### Old:

### Updated:
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
          
        
        
             

## Artifact 2: Algorithms and Datastructures
### Old:

### Updated:

## Artifact 3: Databases
### Old:

### Updated:
