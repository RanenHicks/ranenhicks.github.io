from Contact import Contact

# Declaring variables, removing magic numbers
STORESTASK = 1

class ContactService:

    # Citation for self usage: (Gyanendra371, 2024)

    # (Erakshaya485, 2024), initializes the class.
    def __init__(self, addContact, deleteContact, updateContact, contactList, contactId, contactFirstName, contactLastName, contactPhone, contactDescription):
        if addContact == None:
            return
        
        self.ContactService(addContact, deleteContact, updateContact, contactList, contactId, contactFirstName, contactLastName, contactPhone, contactDescription)

    # Main contact service function
    def ContactService(self, addContact, deleteContact, updateContact, contactList, contactId, contactFirstName, contactLastName, contactPhone, contactDescription):

        self.added = False
        self.deleted = False
        self.updated = False
        contactExists = False

        if len(contactList) >= STORESTASK:

            # Checks if an contact already exists with input id.
            for incrementContactList in contactList:
                if contactId == incrementContactList.getContactId():
                    contactExists = True
        
                else:
                    contactExists = False
        
        # Adding contact
        if addContact == True:
            confirmationContact = self.addingContact(addContact, contactExists, contactId, contactFirstName, contactLastName, contactPhone, contactDescription)

            return confirmationContact

        # Deleting contact
        if deleteContact == True:
            self.deletingContact(deleteContact, contactExists, contactList, contactId)

        # Updating contact
        if updateContact == True:
            self.updatingContact(updateContact, contactExists, contactList, contactId, contactFirstName, contactLastName, contactPhone, contactDescription)
                


    # Adds an contact
    def addingContact(self, addContact, contactExists, contactId, contactFirstName, contactLastName, contactPhone, contactDescription): 
        
        # (Kalra, 2023; Everythingtech, 2023), initializing new contact
        newContact = Contact(None, None, None, None, None, True)

        # (TonyA, 2013; Rollbar Editorial Team, 2023), adding contact with error checking
        try:
            if (addContact == True) and (contactExists == False):
                newContact.Contact(contactId, contactFirstName, contactLastName, contactPhone, contactDescription)
                if newContact.addedCorrectly == False:
                    self.added = False
                    return
                else:
                    self.added = True
                    return newContact
        
        # User incorrect id error check
            elif (addContact == True) and (contactExists == True):
                raise Exception
        except:
            self.added = False
            print("Contact with input id has already been made, please use another id.")

        
    # Deletes a contact.
    def deletingContact(self, deleteContact, contactExists, contactList, contactId): 
        
        # Variable to iterate through contact list to find location of same contact
        sameContactId = 0
        # (TonyA, 2013; Rollbar Editorial Team, 2023), deleting contact with error checking
        try:
            if (deleteContact == True) and (contactExists == True):
                for incrementContactList in contactList:
                    if contactId == incrementContactList.getContactId():
                        contactDelete = contactList.pop(sameContactId)
                        contactDelete.deleteContactInfo()
                        contactDelete = None
                        self.deleted = True
                
                    # Adds one after if statment since the list can store at [0]
                    sameContactId += 1

            # User inccorect id error check
            elif (deleteContact == True) and (contactExists == False):
                raise Exception
        except:
                self.deleted = False
                print("Contact with input id does not exist, can not delete.")

    # Updates a contact.
    def updatingContact(self, updateContact, contactExists, contactList, contactId, contactFirstName, contactLastName, contactPhone, contactDescription): 
        
        # Variable to iterate through contact list to find location of same contact
        sameContactId = 0

        # (TonyA, 2013; Rollbar Editorial Team, 2023), deleting contact with error checking
        try:
            if (updateContact == True) and (contactExists == True):
                for incrementContactList in contactList:
                    if contactId == incrementContactList.getContactId():
                        contactUpdate = contactList.pop(sameContactId)
                        contactUpdate.updateContactInfo(contactFirstName, contactLastName, contactPhone, contactDescription)
                        self.updated = True
                
                    # Adds one after if statment since the list can store at [0]
                    sameContactId += 1

            # User inccorect id error check
            elif (updateContact == True) and (contactExists == False):
                raise Exception
        except:
                self.updated = False
                print("Contact with input id does not exist, can not update.")

        
