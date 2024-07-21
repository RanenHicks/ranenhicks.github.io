from Appointment import Appointment

# Declaring variables, removing magic numbers
STORESAPPOINTMENT = 1

class AppointmentService:

    # Citation for self usage: (Gyanendra371, 2024)

    # (Erakshaya485, 2024), initializes the class.
    def __init__(self, addAppointment, deleteAppointment, appointmentList, appointmentId, appointmentDate, appointmentDescription):
        if addAppointment == None:
            return
        
        self.AppointmentService(addAppointment, deleteAppointment, appointmentList, appointmentId, appointmentDate, appointmentDescription)

    # Main appointment service function
    def AppointmentService(self, addAppointment, deleteAppointment, appointmentList, appointmentId, appointmentDate, appointmentDescription):

        self.added = False
        self.deleted = False
        appointmentExists = False

        if len(appointmentList) >= STORESAPPOINTMENT:

            # Checks if an appointment already exists with input id.
            for incrementAppointmentList in appointmentList:
                if appointmentId == incrementAppointmentList.getAppointmentId():
                    appointmentExists = True
        
                else:
                    appointmentExists = False
        
        # Adding appointment
        if addAppointment == True:
            confirmationAppointment = self.addingAppointment(addAppointment, appointmentExists, appointmentId, appointmentDate, appointmentDescription)
            
            # Test Confirmation
            self.added = True

            return confirmationAppointment

        # Deleting appointment
        if deleteAppointment == True:
            self.deletingAppointment(deleteAppointment, appointmentExists, appointmentList, appointmentId)
                


    # Adds an appointment
    def addingAppointment(self, addAppointment, appointmentExists, appointmentId, appointmentDate, appointmentDescription): 
        
        # (Kalra, 2023; Everythingtech, 2023), initializing new appointment
        newAppointment = Appointment(None, None, None, True)

        # (TonyA, 2013; Rollbar Editorial Team, 2023), adding appointment with error checking
        try:
            if (addAppointment == True) and (appointmentExists == False):
                newAppointment.Appointment(appointmentId, appointmentDate, appointmentDescription)
                return newAppointment
        
        # User incorrect id error check
            elif (addAppointment == True) and (appointmentExists == True):
                raise Exception
        except:
            print("Appointment with input id has already been made, please use another id.")

        
    # Deletes an appointment.
    def deletingAppointment(self, deleteAppointment, appointmentExists, appointmentList, appointmentId): 
        
        # Variable to iterate through appointment list to find location of same appointment
        sameAppointmentId = 0

        # (TonyA, 2013; Rollbar Editorial Team, 2023), deleting appointment with error checking
        try:
            if (deleteAppointment == True) and (appointmentExists == True):
                for incrementAppointmentList in appointmentList:
                    if appointmentId == incrementAppointmentList.appointmentId:
                        appointmentDelete = appointmentList.pop(sameAppointmentId)
                        appointmentDelete.deleteAppointmentInfo()
                        appointmentDelete = None
                        self.deleted = True
                
                    # Adds one after if statment since the list can store at [0]
                    sameAppointmentId += 1

            # User inccorect id error check
            elif (deleteAppointment == True) and (appointmentExists == False):
                raise Exception
        except:
                print("Appointment with input id does not exist, can not delete.")

        
