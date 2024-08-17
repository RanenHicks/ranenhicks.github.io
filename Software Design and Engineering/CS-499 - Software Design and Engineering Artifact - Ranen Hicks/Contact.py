# Declaring variables, removing magic numbers
CONTACTIDNAMEPHONEMAX = 10
CONTACTADDRESSMAX = 30


class Contact:

    # Citation for self usage: (Gyanendra371, 2024)

    # (Erakshaya485, 2024), initializing contact object
    def __init__(self, newContactId, newContactFirstName, newContactLastName, newContactPhone, newContactAddress, newContactInstantce): 
        if newContactInstantce == True:
            return
        
        self.Contact(newContactId, newContactFirstName, newContactLastName, newContactPhone, newContactAddress)

    def Contact(self, newContactId, newContactFirstName, newContactLastName, newContactPhone, newContactAddress):


        # (TonyA, 2013; Rollbar Editorial Team, 2023), contact id being set, and error checking.
        try:
            if len(newContactId) <= CONTACTIDNAMEPHONEMAX:
                self.addedCorrectly = True
                self.contactId = newContactId

            # Too Long of id
            elif len(newContactId) > CONTACTIDNAMEPHONEMAX:
                print("Contact id is too long, please keep it to 10 characters or less.")
                raise Exception
            
            # Null Id
            elif newContactId == None:
                print("Contact id is null, please enter an id.")
                raise Exception
            
        except:
             self.addedCorrectly = False
        
        # Calls functions to set input other information.
        self.setContactFirstName(newContactFirstName)
        self.setContactLastName(newContactLastName)
        self.setContactPhone(newContactPhone)
        self.setContactAddress(newContactAddress)

        # Returns object
        return self 



    # Setters and getters
    def getContactId(self):
          return self.contactId
    
    def getContactFirstName(self):
        return self.contactFirstName

    def setContactFirstName(self, newContactFirstname):
        try:
            if len(newContactFirstname) <= CONTACTIDNAMEPHONEMAX:
                self.contactFirstName = newContactFirstname
                # First Name is too big
            elif len(newContactFirstname) > CONTACTIDNAMEPHONEMAX:
                print("Contact first name is too big, please try again.")
                raise Exception
                
            # Null first name input
            elif newContactFirstname == None:
                print("Contact first name is empty, please try again.")
                raise Exception
        except:
            self.addedCorrectly = False # Flags incorrect data
        
    def getContactLastName(self):
        return self.contactLastName

    def setContactLastName(self, newContactLastname):
        try:
            if len(newContactLastname) <= CONTACTIDNAMEPHONEMAX:
                self.contactLastName = newContactLastname
                # Last name is too big
            elif len(newContactLastname) > CONTACTIDNAMEPHONEMAX:
                print("Contact first name is too big, please try again.")
                raise Exception
                
            # Null last name input
            elif newContactLastname == None:
                print("Contact first name is empty, please try again.")
                raise Exception
        
        except:
            self.addedCorrectly = False # Flags incorrect data
        

    def getContactPhone(self):
          return self.contactPhone
    
    def setContactPhone(self, newContactPhone):

        
        # (TonyA, 2013; Rollbar Editorial Team, 2023), Sets contact date if is valid.
        try:
            if len(newContactPhone) == CONTACTIDNAMEPHONEMAX:
                self.contactPhone = newContactPhone
            
            # Phone number is too big
            elif len(newContactPhone) > CONTACTIDNAMEPHONEMAX:
                print("Contact phone number is too big, please try again.")
                raise Exception
            
            # Phone number is too small
            elif len(newContactPhone) < CONTACTIDNAMEPHONEMAX:
                print("Contact phone number is too small, please try again.")
                raise Exception
            
            # Null phone number input
            elif newContactPhone == None:
                print("Contact phone number is empty, please try again.")
                raise Exception
        except:
             self.addedCorrectly = False # Flags incorrect data
                
            

    def getContactAddress(self):
          return self.contactAddress
    
    def setContactAddress(self, newContactAddress):

        # (TonyA, 2013; Rollbar Editorial Team, 2023), contact address being set as well as error checking.
        try:
            if len(newContactAddress) <= CONTACTADDRESSMAX:
                self.contactAddress = newContactAddress

            # Address too long
            elif len(newContactAddress) > CONTACTADDRESSMAX:
                print("Contact address is too long, please keep it to 30 characters or less.")
                raise Exception
            
            # Null address input
            elif newContactAddress.equals(None):
                print(("Contact address is null, please enter an address."))
                raise Exception
        except:
            self.addedCorrectly = False # Flags incorrect data
    
    # Function deletes information stored within object
    def deleteContactInfo(self):
          self.contactId = None
          self.contactFirstName = None
          self.contactLastName = None
          self.contactPhone = None
          self.contactAddress = None
    
    # Function updates information within object.
    def updateContactInfo(self, newContactFirstName, newContactLastName, newContactPhone, newContactAddress):
        self.contactPhone = self.setContactFirstName(newContactFirstName)
        self.contactAddress = self.setContactLastName(newContactLastName)
        self.contactPhone = self.setContactPhone(newContactPhone)
        self.contactAddress = self.setContactAddress(newContactAddress)
        
        
             