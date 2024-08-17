import unittest
from Appointment import Appointment
from AppointmentService import AppointmentService
import datetime

class AppointmentTests (unittest.TestCase):

    # Appointment Service add tests
    def testAppointmentServiceAddCorrect(self):
        
        # Initializing empty list for test
        checkAppointmentList = []

        # # (Kalra, 2023; Everythingtech, 2023), initializing and entering correct info into the appointment service
        checkAppointmentServices = AppointmentService(None, None, None, None, None, None)
        checkAppointmentServices.AppointmentService(True, False, checkAppointmentList, "1", datetime.date(2025, 1, 1), "1")
        
        # Checks added variable to see if addition happened
        self.assertEqual(checkAppointmentServices.added, True)
    
    def testAppointmentServiceAddIdIncorrect(self):
        
        # Creating appointment test list
        checkAppointmentList = []

        # (Kalra, 2023; Everythingtech, 2023), creates an existing appointment and stores it
        checkAppointment = Appointment(None, None, None, True)
        checkAppointment.Appointment("1", datetime.date(2025, 1, 1), "1")
        checkAppointmentList.append(checkAppointment) 

        # Initializes appointment services
        checkAppointmentServices = AppointmentService(None, None, checkAppointmentList, None, None, None)
        
        # Inputs incorrect addition information into appointment services
        checkAppointmentServices.AppointmentService(True, False, checkAppointmentList, "1", datetime.date(2025, 1, 1), "1")
        
        # Checks added variable to see if addition happened
        self.assertFalse(checkAppointmentServices.added)

    
    # Delete tests
    def testAppointmentServiceDeleteCorrect(self):
        
        # Creating appointment test list
        checkAppointmentList = []

        # (Kalra, 2023; Everythingtech, 2023), creates an existing appointment and stores it
        checkAppointment = Appointment(None, None, None, True)
        checkAppointment.Appointment("1", datetime.date(2025, 1, 1), "1")
        checkAppointmentList.append(checkAppointment) 

        # Initializes appointment services and inputs correct deletion information
        checkAppointmentServices = AppointmentService(None, None, checkAppointmentList, None, None, None)
        checkAppointmentServices.AppointmentService(False, True, checkAppointmentList, "1", None, None)
        
        # Checks added variable to see if deletion happened
        self.assertEqual(checkAppointmentServices.deleted, True)

    def testAppointmentServiceDeleteIdIncorrect(self):
        
        # Creating appointment test list
        checkAppointmentList = []

        # (Kalra, 2023; Everythingtech, 2023), initializes appointment services
        checkAppointmentServices = AppointmentService(None, None, checkAppointmentList, None, None, None)
        
        # Inputs incorrect deletion information and checks for non-deletion
        checkAppointmentServices.AppointmentService(False, True, checkAppointmentList, "2", None, None)
        self.assertFalse(checkAppointmentServices.deleted)


# Starts unit tests        
if __name__== '__main__':
    unittest.main()