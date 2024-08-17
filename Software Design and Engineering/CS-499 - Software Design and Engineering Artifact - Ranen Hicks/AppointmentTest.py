import unittest
from Appointment import Appointment
import datetime

class AppointmentTests (unittest.TestCase):

    # Test with all information correct
    def testAppointmentAllCorrect(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises appointment
        checkAppointment = Appointment(None, None, None, True)
        checkAppointment.Appointment("1", datetime.date(2025, 1, 1), "1")
    
        # Checks appointment information
        self.assertEqual(checkAppointment.getAppointmentId(), "1")
        self.assertEqual(checkAppointment.getAppointmentDate(), datetime.date(2025, 1, 1))
        self.assertEqual(checkAppointment.getAppointmentDescription(), "1")
        self.assertTrue(checkAppointment.addedCorrectly)


    # Appointment id tests
    def testAppointmentIdLong(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises appointment
        checkAppointment = Appointment(None, None, None, True)

        # Checks if appointment was not added
        self.assertFalse(checkAppointment.Appointment("11111111111", datetime.date(2025, 1, 1), "1").addedCorrectly)


    def testAppointmentIdNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises appointment
        checkAppointment = Appointment(None, None, None, True)

        # Checks if appointment was not added
        self.assertFalse(checkAppointment.Appointment(None, datetime.date(2025, 1, 1), "1").addedCorrectly)


    # Appointment date tests
    def testAppointmentDateBeforeCurrent(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises appointment
        checkAppointment = Appointment(None, None, None, True)

        # Checks if appointment was not added
        self.assertFalse(checkAppointment.Appointment("1", datetime.date(2023, 1, 1), "1").addedCorrectly)


    def testAppointmentDateNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises appointment
        checkAppointment = Appointment(None, None, None, True)

        # Checks if appointment was not added
        self.assertFalse(checkAppointment.Appointment("1", None, "1").addedCorrectly)


    # Appointment description test
    def testAppointmentDescriptionLong(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises appointment
        checkAppointment = Appointment(None, None, None, True)

        # Checks for addition of appointment
        self.assertFalse(checkAppointment.Appointment("1", datetime.date(2025, 1, 1), (51 * "1")).addedCorrectly)


    def testAppointmentDescriptionNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises appointment
        checkAppointment = Appointment(None, None, None, True)

       # Checks for addition of appointment
        self.assertFalse(checkAppointment.Appointment("1", datetime.date(2025, 1, 1), None).addedCorrectly)
 
        
# Calls the unit tests
if __name__== '__main__':
    unittest.main()