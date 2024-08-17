
public class ContactService {
	
	// Creating boolean checks for the functions in this class.
	static public boolean added;
	static public boolean updated;
	static public boolean deleted;
	
	public ContactService(boolean add, boolean delete, boolean update, String id, String fName, String lName, String phoneNum, String addressContact) {
		
		// Would create an empty contact for possible editing, not needed in this assignment I believe. Also the Contact().
		//Contact contactUpdateDel = new Contact();
		
		// Keeps track if there already is a contact with the same Id.
		boolean sameId = false;
		
		// Incrementing variable for fake loop.
		int i = 0;
		
		// Creates a contact for updating and deleting. Also for id testing.
		Contact contact = new Contact("1", "1", "1", "1111111111", "1");
		
		// While loop would check if there is an identical id already.
		/*
		while (i < contactloop.length()) {
			if (contactLoop[i].getContactId() == id ) {
				sameId = true;
				contactUpdateDel = contactLoop[i];
			}
			
			i++;
		}
		*/
		
		// Just checks if id inputed is same with the one already implemented above.
		if (contact.getContactId() == id) {
			sameId = true;
		}
		
		// Checks if user wants to add a contact and checks if there already was a contact with the same id.
		if (true == add && sameId == false) {
			added = addContact(id, fName, lName, phoneNum, addressContact);
		}
		
		// Tells the user that there already is a contact with the same Id.
		else if (add == true && sameId == true) {
			throw new IllegalArgumentException("Already have a contact with the same Id.");
		}
		
		// Checks if the id correlates to a contact and deletes it if the user wants the contact to be deleted.
		if (true == delete && sameId == true) {
			
			// Deletes contact.
			deleted = deleteContact(contact);
			// Would be deleteContact(contactUpdateDel); if was the complete program
		}
		
		// If user wanted to delete contact but did not have the correct id, an error will be thrown to the user.
		else if (true == delete && sameId == false) {
			throw new IllegalArgumentException("Cannot delete as there is no contact with the same Id.");
		}
		
		// Checks if the id correlates to a contact and updates it with the input.
		if (true == update && sameId == true) {
			
			// Updates contact.
			updated = updateContact(contact, fName, lName, phoneNum, addressContact);
			// Similarly to delete, this in a full program would be different and would be something like:
			// updateContact(contactUpdateDel, fName, lName, phoneNum, addressContact);
		}
		
		// If user wanted to update the contact, but does not have the correct id, an error will be thrown to the user.
		else if (true == update && sameId == false) {
			throw new IllegalArgumentException("Cannot update the contact as there is no contact with the same Id.");
		}
	}
		
	
	
	// Adding/creating a new contact.
	public boolean addContact(String id, String fName, String lName, String phoneNum, String addressContact) {
		
		// Adding the contact using the information inputed.
		try {
			Contact contact = new Contact(id, fName, lName, phoneNum, addressContact);
			// Would add contact to the contact list or something similar.
			// contactLoop.addContact(contact);
			}
		
			// Checks if the contact was added correctly and returns true or false based off if it was or not.
			catch (IllegalArgumentException e) {
				return false;
		}
		
		return true;
	}
	
	// Deletes contact info
	public boolean deleteContact(Contact contact) {
		
		// Deleting contact info
		contact = contact.contactDelete(contact);
		
		// Checks if the first name can be grabbed, as that would mean deletion failed
		try {
			contact.getFirstName();
			}
		
		// If argument is caught, deletion worked.
		catch (NullPointerException e) {
			return true;
			}
		
		// Otherwise deletion did not work.
		return false;
	}
	
	// Updating contact information.
	public boolean updateContact (Contact contact, String fName, String lName, String phoneNum, String addressContact) {
		
		try {
			// Setting the values of the contact to the new input.
			contact.setFirstName(fName);
			contact.setLastName(lName);
			contact.setPhone(phoneNum);
			contact.setAddress(addressContact);
		}
		
		// Checks if the contact was updated correctly.
		catch (IllegalArgumentException e) {
			
			// If it was not false will be returned
			return false;
		}
		
	// Otherwise true will be returned.
	return true;
	}
}
