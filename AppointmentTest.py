import unittest
from Appointment import Appointment
import datetime

class AppointmentTests (unittest.TestCase):

    # Test with all information correct
    def testAppointmentAllCorrect(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises appointment.
        checkAppointment = Appointment(None, None, None, True)
        checkAppointment.Appointment("1", datetime.date(2025, 1, 1), "1")
        
        self.assertEqual(checkAppointment.getAppointmentId(), "1")
        self.assertEqual(checkAppointment.getAppointmentDate(), datetime.date(2025, 1, 1))
        self.assertEqual(checkAppointment.getAppointmentDescription(), "1")

    # Appointment id tests
    def testAppointmentIdLong(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises appointment.
        checkAppointment = Appointment(None, None, None, True)

        with self.assertRaises(Exception):
            checkAppointment.Appointment("11111111111", datetime.date(2025, 1, 1), "1")

    def testAppointmentIdNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises appointment.
        checkAppointment = Appointment(None, None, None, True)

        with self.assertRaises(Exception):
            checkAppointment.Appointment(None, datetime.date(2025, 1, 1), "1")

    # Appointment date tests
    def testAppointmentDateBeforeCurrent(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises appointment.
        checkAppointment = Appointment(None, None, None, True)

        with self.assertRaises(Exception):
            checkAppointment.Appointment("1", datetime.date(2023, 1, 1), "1")

    def testAppointmentDateNull(self):
        checkAppointment = Appointment(None, None, None, True)

        with self.assertRaises(Exception):
            checkAppointment.Appointment("1", None, "1")

    # Appointment description test
    def testAppointmentDescriptionLong(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises appointment.
        checkAppointment = Appointment(None, None, None, True)

        with self.assertRaises(Exception):
            checkAppointment.Appointment("1", datetime.date(2025, 1, 1), "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")

    def testAppointmentDescriptionNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises appointment.
        checkAppointment = Appointment(None, None, None, True)

        with self.assertRaises(Exception):
            checkAppointment.Appointment("1", datetime.date(2025, 1, 1), None)
        

if __name__== '__main__':
    unittest.main()