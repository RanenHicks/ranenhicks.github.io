
public class Contact {
	
	// Creating private variables for the contact information
	private String contactId;
	private String firstName;
	private String lastName;
	private String phone;
	private String address;
	
	public Contact(String id, String fName, String lName, String phoneNum, String addressContact) {
		setContactId(id);
		setFirstName(fName);
		setLastName(lName);
		setPhone(phoneNum);
		setAddress(addressContact);
	}
	
	// Deletes the contact's info and the contact itself.
	public Contact contactDelete (Contact contactDeleted) {
		contactDeleted.firstName = null;
		contactDeleted.lastName = null;
		contactDeleted.phone = null;
		contactDeleted.address = null;
		contactDeleted = null;
		return contactDeleted;
		
	}
	
	// Creating getters and setters for each of the variables/pieces of info we need to store.
	public String getContactId() {
		return contactId;
	}
	
	public void setContactId(String Id) {
		
		// Checks if the id is 10 characters or less, and if it is more, then an exception will be sent.
		try {
			if (Id.length() < 11) {
				contactId = Id;
			}
			else {
				throw new IllegalArgumentException("Invalid id");
			}
		}
		
		// Checks for null input and throws exception
		catch (NullPointerException e) {
			throw new IllegalArgumentException("Invalid First Name");
		}
	}
	
	public String getFirstName() {
		return firstName;
	}
	
	public void setFirstName (String fName) {
		
		// Checks if the first name inputed is the correct length and sets the value accordingly.
		try {
			if (fName.length() < 11) {
				firstName = fName;
			}
			else {
			// Exception is thrown because input is invalid
				throw new IllegalArgumentException("Invalid First Name");
			}
		}	
		
		// Checks for null input and throws exception
		catch (NullPointerException e) {
			throw new IllegalArgumentException("Invalid First Name");
		}
	}
	
	public String getLastName() {
		return lastName;
	}
	
	public void setLastName(String lName) {
		
		// Checks if the last name inputed is the correct length and sets the value accordingly.
		try {
			if (lName.length() < 11) {
				lastName = lName;
			}
			else {
			
				// Exception is thrown because input is invalid
				throw new IllegalArgumentException("Invalid Last Name");
			}
		}
		
		// Checks for null input and throws exception
		catch (NullPointerException e) {
			throw new IllegalArgumentException("Invalid First Name");
		}
		
	}
	
	public String getPhone() {
		return phone;
	}
	
	public void setPhone(String phoneNumber) {
		
		// Checks if the phone number is the correct length and checks if all the values are numbers
				try {
					if ((phoneNumber.length() == 10) && (phoneNumber.toUpperCase() == phoneNumber.toLowerCase())) {
						phone = phoneNumber;
					}
				
					// If the phone number is not valid it will be sent to this else statement.
					else {
					
						// Exception is thrown because input is invalid
						throw new IllegalArgumentException("Invalid Phone Number");
					}
				}
				
				// Checks for null input and throws exception
				catch (NullPointerException e) {
					throw new IllegalArgumentException("Invalid Phone Number");
				}
	}
	
	public String getAddress() {
		return address;
	}
	
	public void setAddress(String addressForContact) {

		// Checks if the phone number is the correct length and sets the address to the input if so.
		try {
			if (addressForContact.length() < 31) {
				address = addressForContact;
			}
		
			// If the address the user inputed is not valid it will be sent to this else statement.
			else {
			
				// Exception is thrown because input is invalid
				throw new IllegalArgumentException("Invalid Address");
			}
		}
		
		// Checks for null input and throws exception
		catch (NullPointerException e) {
			throw new IllegalArgumentException("Invalid First Name");
		}
	}
}
