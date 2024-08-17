import unittest
from Contact import Contact

class ContactTests (unittest.TestCase):

    # Test with all information correct
    def testContactAllCorrect(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Contact
        checkContact = Contact(None, None, None, None, None, True)
        checkContact.Contact("1", "1", "1", "1111111111", "1")
    
        # Checks Contact information
        self.assertEqual(checkContact.getContactId(), "1")
        self.assertEqual(checkContact.getContactFirstName(), "1")
        self.assertEqual(checkContact.getContactLastName(), "1")
        self.assertEqual(checkContact.getContactPhone(), "1111111111")
        self.assertEqual(checkContact.getContactAddress(), "1")
        self.assertTrue(checkContact.addedCorrectly)


    # Contact id tests
    def testContactIdLong(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Contact
        checkContact = Contact(None, None, None, None, None, True)

        # Checks if Contact was not added
        self.assertFalse(checkContact.Contact("11111111111", "1", "1", "1111111111", "1").addedCorrectly)


    def testContactIdNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Contact
        checkContact = Contact(None, None, None, None, None, True)

        # Checks if Contact was not added
        self.assertFalse(checkContact.Contact(None, "1", "1", "1111111111", "1").addedCorrectly)


    # Contact date tests
    def testContactPhoneSmall(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Contact
        checkContact = Contact(None, None, None, None, None, True)

        # Checks if Contact was not added
        self.assertFalse(checkContact.Contact("1", "1", "1", "111111111", "1").addedCorrectly)
    
    def testContactPhoneBig(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Contact
        checkContact = Contact(None, None, None, None, None, True)

        # Checks if Contact was not added
        self.assertFalse(checkContact.Contact("1", "1", "1", "11111111111", "1").addedCorrectly)


    def testContactPhoneNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Contact
        checkContact = Contact(None, None, None, None, None, True)

        # Checks if Contact was not added
        self.assertFalse(checkContact.Contact("1", "1", "1", None, "1").addedCorrectly)


    # Contact description test
    def testContactAddressLong(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Contact
        checkContact = Contact(None, None, None, None, None, True)

        # Checks for addition of Contact
        self.assertFalse(checkContact.Contact("1", "1", "1", "1111111111", (51 * "1")).addedCorrectly)


    def testContactAddressNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Contact
        checkContact = Contact(None, None, None, None, None, True)

       # Checks for addition of Contact
        self.assertFalse(checkContact.Contact("1", "1", "1", "1111111111", None).addedCorrectly)
 
        
# Calls the unit tests
if __name__== '__main__':
    unittest.main()