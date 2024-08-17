import unittest
from Contact import Contact
from ContactService import ContactService

class ContactTests (unittest.TestCase):

    # Contact Service add tests
    def testContactServiceAddCorrect(self):
        
        # Initializing empty list for test
        checkContactList = []

        # # (Kalra, 2023; Everythingtech, 2023), initializing and entering correct info into the Contact service
        checkContactServices = ContactService(None, None, None, checkContactList, None, None, None, None, None)
        checkContactServices.ContactService(True, False, False, checkContactList, "1", "1", "1", "1111111111", "1")
        
        # Checks added variable to see if addition happened
        self.assertEqual(checkContactServices.added, True)
    
    def testContactServiceAddIdIncorrect(self):
        
        # Creating Contact test list
        checkContactList = []

        # (Kalra, 2023; Everythingtech, 2023), creates an existing Contact and stores it
        checkContact = Contact(None, None, None, None, None, True)
        checkContact.Contact("1", "1", "1", "1111111111", "1")
        checkContactList.append(checkContact) 

        # Initializes Contact services
        checkContactServices = ContactService(None, None, None, checkContactList, None, None, None, None, None)
        
        # Inputs incorrect addition information into Contact services
        checkContactServices.ContactService(True, False, False, checkContactList, "1", "1", "1", "1111111111", "1")
        
        # Checks added variable to see if addition happened
        self.assertFalse(checkContactServices.added)

    
    # Delete tests
    def testContactServiceDeleteCorrect(self):
        
        # Creating Contact test list
        checkContactList = []

        # (Kalra, 2023; Everythingtech, 2023), creates an existing Contact and stores it
        checkContact = Contact(None, None, None, None, None, True)
        checkContact.Contact("1", "1", "1", "1111111111", "1")
        checkContactList.append(checkContact) 

        # Initializes Contact services and inputs correct deletion information
        checkContactServices = ContactService(None, None, None, checkContactList, None, None, None, None, None)
        checkContactServices.ContactService(False, True, False, checkContactList, "1", "1", "1", "1111111111", "1")
        
        # Checks added variable to see if deletion happened
        self.assertEqual(checkContactServices.deleted, True)

    def testContactServiceDeleteIdIncorrect(self):
        
        # Creating Contact test list
        checkContactList = []

        # (Kalra, 2023; Everythingtech, 2023), initializes Contact services
        checkContactServices = ContactService(None, None, None, checkContactList, None, None, None, None, None)
        
        # Inputs incorrect deletion information and checks for non-deletion
        checkContactServices.ContactService(False, True, False, checkContactList, "2", None, None, None, None)
        self.assertFalse(checkContactServices.deleted)


    # Update tests
    def testContactServiceUpdateCorrect(self):
        
        # Creating Contact test list
        checkContactList = []

        # (Kalra, 2023; Everythingtech, 2023), creates an existing Contact and stores it
        checkContact = Contact(None, None, None, None, None, True)
        checkContact.Contact("1", "1", "1", "1111111111", "1")
        checkContactList.append(checkContact) 

        # Initializes Contact services and inputs correct deletion information
        checkContactServices = ContactService(None, None, None, checkContactList, None, None, None, None, None)
        checkContactServices.ContactService(False, False, True, checkContactList, "1", "1", "1", "1111111111", "1")
        
        # Checks added variable to see if deletion happened
        self.assertEqual(checkContactServices.updated, True)

    def testContactServiceUpdateIdIncorrect(self):
        
        # Creating Contact test list
        checkContactList = []

        # (Kalra, 2023; Everythingtech, 2023), initializes Contact services
        checkContactServices = ContactService(None, None, None, checkContactList, None, None, None, None, None)
        
        # Inputs incorrect update.
        checkContactServices.ContactService(False, False, True, checkContactList, "2", None, None, None, None)
        self.assertFalse(checkContactServices.updated)

# Starts unit tests        
if __name__== '__main__':
    unittest.main()