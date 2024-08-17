<!-- (Github basic writing and formatting syntax, n.d.; pierrejoubert73, 2024) -->
# Software Development and Engineering
## [See the Artifacts in the Repository](https://github.com/RanenHicks/ranenhicks.github.io/tree/main/Software%20Design%20and%20Engineering)

## Click to navigate:
### [Old Artifact](#old-artifact)

# Old Artifact (CS 340 Artifact Without Enhancements):
## Appointment Services:

### Appointment.java

```java
import java.util.Date;

public class Appointment {
	
	// Private variables for appointment class.
	private String appointmentId;
	private Date appointmentDate;
	private String appointmentDescription;
	
	// Constructor for new appointment object
	public Appointment(String newAppointmentId, Date newAppointmentDate, String newAppointmentDescription) {
		
		// Checks if the appointment Id is valid and will send errors if it is not.
		try {
			
			// Checks if the new appointment is the correct length.
			if (newAppointmentId.length() < 11) {
				
				// Sets the id if it is valid.
				appointmentId = newAppointmentId;
			}
			
			else if (newAppointmentId.length() > 10) {
				throw new IllegalArgumentException("Invalid Id");
			}
		}
		
		// Sees if the date was null and sends error if so.
		catch(NullPointerException e) {
			throw new IllegalArgumentException("Null Appointment Id");
		}
		
		// Sets appointment date and description.
		setAppointmentDate(newAppointmentDate);
		setAppointmentDescription(newAppointmentDescription);
	}
	
	// Gets the appointment id when it is needed. Most likely will not be used.
	public String getAppointmentId() {
		return appointmentId;
	}
	
	// Sets the appointment date to the new appointment date.
	public void setAppointmentDate(Date newAppointmentDate) {
		
		// Checks if the appointment date is valid.
		try {
			
			// Checks if the date is before the date today.
			if (false == newAppointmentDate.before(new Date())) {
				appointmentDate = newAppointmentDate;
			}
			
			// Throws that error that the date already passed.
			else {
				throw new IllegalArgumentException("Date Already Passed");
			}
			
		// Throws the null error if the date was null.
		}
		catch (NullPointerException e) {
			throw new IllegalArgumentException("Date Was Null");
		}
	}
	
	// Gets the appointment date when it is needed.
		public Date getAppointmentDate() {
			return appointmentDate;
		}
		
		// Sets the appointment description to the new appointment date.
		public void setAppointmentDescription(String newAppointmentDescription) {
			
			// Checks if the appointment description is valid.
			try {
				
				// Checks if the description is the correct length.
				if (newAppointmentDescription.length() < 51) {
					appointmentDescription = newAppointmentDescription;
				}
				
				// Throws that error that the description is too long.
				else {
					throw new IllegalArgumentException("Description Is Too Long");
				}
				
			// Throws the null error if the description was null.
			}
			catch (NullPointerException e) {
				throw new IllegalArgumentException("Description Was Null");
			}
		}
		
		// Gets the appointment description when it is needed.
		public String getAppointmentDescription() {
			return appointmentDescription;
		}
		
		// Deletes info off of appointment.
		public void deleteAppointment() {
			appointmentId = null;
			appointmentDescription= null;
			appointmentDate = null;
		}
}
```

### AppointmentTest.java
```java
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import java.util.Date;

class AppointmentTest {

	
	// Checks if everything works correctly with correct input.
	@Test
	void appointmentCorrectTest() {
		Date check = new Date(200, 11, 11);
		Appointment newAppointment = new Appointment("1", check, "11111");
		assertTrue(newAppointment.getAppointmentDate().equals(check));
		assertTrue(newAppointment.getAppointmentId().equals("1"));
		assertTrue(newAppointment.getAppointmentDescription().equals("11111"));
	}
	
	// Tests when the id is too long.
	@Test
	void appointmentInvalidIdTest() {
		Date check = new Date(200, 11, 11);
		Assertions.assertThrows(IllegalArgumentException.class,() -> {
				new Appointment("11111111111", check, "11111"); 
				});
	}
	
	// Null id test.
	@Test
	void appointmentNullIdTest() {
		Date check = new Date(200, 11, 11);
		Assertions.assertThrows(IllegalArgumentException.class,() -> {
				new Appointment(null, check, "11111"); 
				});
	}
	
	// Date before test.
	@Test
	void appointmentDateBeforeTest() {
		Date check = new Date();
		check.setTime(111111);
		Assertions.assertThrows(IllegalArgumentException.class,() -> {
				new Appointment("1", check, "11111"); 
				});
	}
	
	// Date null test.
	@Test
	void appointmentDateNullTest() {
		Assertions.assertThrows(IllegalArgumentException.class,() -> {
				new Appointment("1", null, "11111"); 
				});
	}
	
	// Description null test.
	@Test
	void appointmentDescriptionNullTest() {
		Date check = new Date(200, 11, 11);
		Assertions.assertThrows(IllegalArgumentException.class,() -> {
				new Appointment("1", check, null); 
				});
	}
	
	// Description too many characters test.
	@Test
	void appointmentDescriptionInvalidTest() {
		Date check = new Date(200, 11, 11);
		Assertions.assertThrows(IllegalArgumentException.class,() -> {
				new Appointment("1", check, "111111111111111111111111111111111111111111111111111"); 
				});
	}


}
```

### AppointmentService.java
  
```java
import java.util.Date;

public class AppointmentService {
	
	public boolean added;
	public boolean deleted;
	
	// Constructor for appointment service object.
	public AppointmentService(boolean add, boolean delete, String id, Date date, String description) {
		
		// Makes an appointment for testing.
		Appointment oldAppointment = new Appointment("1", new Date(), "111");
		Appointment newAppointment = null;
		
		// Checks if a new appointment should be added.
		if (add == true && id != oldAppointment.getAppointmentId()) {
			newAppointment = new Appointment(id, date, description);
			added = true;
		}
		
		// The id was the same as a previous one so throws an error.
		else if (add == true) {
			throw new IllegalArgumentException("Id Already Has Appointment.");
		}
		
		// Checks if a new appointment should be deleted.
		if (delete == true) {
			
			// Deletes either of the appointments.
			if (added == true && id == newAppointment.getAppointmentId()) {
				newAppointment.deleteAppointment();
				newAppointment = null;
				deleted = true;
			}
			else if (id == oldAppointment.getAppointmentId()) {
				oldAppointment.deleteAppointment();
				oldAppointment = null;
				deleted = true;
			}
			
			// Throws error when there is no appointment to delete by that id
			else if (delete = true) {
				throw new IllegalArgumentException("No Appointment With Same Id");
			}
		}
	}
}
  ```

### AppointmentServiceTest.java 

```java
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Date;

class AppointmentServiceTest {

	// Checks if the program can add a appointment with the correct information.
	@Test
	void testAppointmentServiceAddCorrect() {
		AppointmentService appointmentServiceTest = new AppointmentService(true, false, "2", new Date(200, 11, 11), "22");
		assertTrue(appointmentServiceTest.added);
	}
	
	// Checks if the program can add a appointment with invalid id.
	@Test
	void testAppointmentServiceAddInvalidId() {
		Assertions.assertThrows(IllegalArgumentException.class, ()-> {
		new AppointmentService(true, false, "1", new Date(200, 11, 11), "22");
		});
	}
	
	// Checks if the program can delete a appointment with the correct information, old appointment.
	@Test
	void testAppointmentServiceDeleteCorrectOld() {
		AppointmentService appointmentServiceTest = new AppointmentService(false, true, "1", new Date(), "22");
		assertTrue(appointmentServiceTest.deleted);
	}
	
	// Checks if the program can delete a appointment with the correct information, new appointment.
	@Test
	void testAppointmentServiceDeleteCorrectNew() {
		AppointmentService appointmentServiceTest = new AppointmentService(true, true, "2", new Date(200, 11, 11), "22");
		assertTrue(appointmentServiceTest.deleted);
	}
	
	// Checks if the program can delete a appointment with invalid id.
	@Test
	void testAppointmentServiceDeleteInvalidId() {
		Assertions.assertThrows(IllegalArgumentException.class, ()-> {
		new AppointmentService(false, true, "2", new Date(200, 11, 11), "22");
		});
	}
}
```

## Contact Services:

### Contact.java

```java

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
```

### ContactTest.java

```java
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class ContactTest {

	@Test
	void testAllCorrect() {
		
		// Checks if the contact class works correctly with correct input
		Contact contact = new Contact("209", "11", "11", "1111111111", "1111");
		assertTrue(contact.getContactId().equals("209"));
		assertTrue(contact.getFirstName().equals("11"));
		assertTrue(contact.getLastName().equals("11"));
		assertTrue(contact.getPhone().equals("1111111111"));
		assertTrue(contact.getAddress().equals("1111"));
	}
	
	// Id
	
	@Test
	void testIdIncorretTooMany() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("toomanyvals", "11", "11", "1111111111", "1111");
		});
	}
	@Test
	void testIdIncorretNull() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact(null, "11", "11", "1111111111", "1111");
		});
	}
	
	// First Name
	@Test
	void testFirstNameIncorretTooMany() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "toomanyvals", "11", "1111111111", "1111");
		});
	}
	
	@Test
	void testFirstNameIncorretNull() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", null, "11", "1111111111", "1111");
		});
	}
	
	//Last Name
	
	@Test
	void testLastNameIncorretTooMany() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", "toomanyvals", "1111111111", "1111");
		});
	}
	
	@Test
	void testLastNameIncorretNull() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", null, "1111111111", "1111");
		});
	}
	
	//Phone
	@Test
	void testPhoneIncorrectNotNumbers() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", "11", "1111111hi1", "1111");
		});	
	}
	
	@Test
	void testPhoneIncorretNull() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", "11", null, "1111");
		});
	}
	
	@Test
	void testPhoneIncorrectTooMany() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", "11", "11111111111", "1111");
		});
	}
	
	// Address
	
	@Test
	void testAddressncorretTooMany() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", "11", "1111111111", "toomanyvals11111111111111111111");
		});
	}
	
	@Test
	void testAddressIncorretNull() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", "11", "1111111111", null);
		});
	}
}
```

### ContactService.java

```java

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
```

### ContactServiceTest.java

```java
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class ContactServiceTest {

	// Add Function tests.
	
	//Everything is correct.
	@Test
	void testAddCorrect() {
		ContactService contactService =  new ContactService (true, false, false, "2", "22", "22", "2222222222", "2222");
		assertTrue(ContactService.added);
	}
	
	// Phone Number is invalid checking if add function detects the error.
	@Test
	void testAddIncorrectInvalidInputToAdd() {
		ContactService contactService =  new ContactService (true, false, false, "2", "22", "22", "22222222222", "2222");
		assertFalse(ContactService.added);
	}
	
	// Same id as contact in contact service, should lead to error.
	@Test
	void testAddIncorrectInvalidInputSameId() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
		ContactService contactService =  new ContactService (true, false, false, "1", "22", "22", "22222222222", "2222");
		});
	}	
	
	// Delete function tests.
	
	// Checks if the specified contact object was deleted. Deletion worked.
	@Test
	void testDeleteCorrect() {
		ContactService contactService =  new ContactService (false, true, false, "1", null, null, null, null);
		assertTrue(ContactService.deleted);
	}
	
	
	// Invalid Id causes deletion to not work.
	@Test
	void testDeleteIncorrectId() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
		ContactService contactService =  new ContactService (false, true, false, "2", null, null, null, null);
		});
	}
	
	// Update function tests.
	
	//Everything is correct.
	@Test
	void testUpdateCorrect() {
		ContactService contactService =  new ContactService (false, false, true, "1", "22", "22", "2222222222", "2222");
		assertTrue(ContactService.updated);
	}
	
	// Phone Number is invalid checking if update function detects the error.
	@Test
	void testUpdateIncorrectInvalidInputToUpdate() {
		ContactService contactService =  new ContactService (false, false, true, "1", "22", "22", "22222222222", "2222");
		assertFalse(ContactService.updated);
	}
	
	// Different id as contact in contact service, should lead to error.
	@Test
	void testUpdateIncorrectInvalidInputSameId() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
		ContactService contactService =  new ContactService (false, false, true, "2", "22", "22", "22222222222", "2222");
		});
	}	
	
}
```

## Task Services:

### Task.java

```java

public class Task {
	
	// Private variables for task class.
	private String taskId;
	private String name;
	private String description;
	
	// Constructor for task class.
	public Task (String newTaskId, String newName, String newDescription) {
		
		try {
			// Checks if the task id is too long.
			if (newTaskId.length() < 11 && newTaskId != null) {
			
				// Sets task id to inputed value.
				taskId = newTaskId;
			}
		
			// If the id is too long, then an error will be thrown
			else {
				throw new IllegalArgumentException("Id is too long.");
			}
		
			// Checks if the name for the task is too long.
			if (newName.length() < 21 && newName != null) {
			
				// Sets the name of task object to inputed value.
				setName(newName);
			}
		
			// If the name for the object is too long, then an error will be thrown
			else {
				throw new IllegalArgumentException("Name is too long.");
			}
			
			// Checks if the description for the task is too long.
			if (newDescription.length() < 51 && newDescription != null) {
			
				// Sets the description of task object to inputed value.
				setDescription(newDescription);
			}
		
			// If the description is too long, then an error will be thrown
			else {
				throw new IllegalArgumentException("Description is too long.");
			}
			
		}
		
		// Checks if a null value was inputed as a variable, and will throw a error if so.
		catch (NullPointerException e) {
			throw new IllegalArgumentException("One of the inputed task values is null.");
		}
	}
	
	// Gets the task id and returns it.
	// Will not have a set function for id as it should not be changed
	public String getTaskId() {
		return taskId;
	}
	
	// Sets the name to the inputed value.
	public void setName(String newName) {
		name = newName;
	}
	
	// Gets the name and returns it.
	public String getName() {
		return name;
	}
	
	// Sets the description to the inputed value.
	public void setDescription (String newDescription) {
		description = newDescription;
	}
	
	// Gets the name and returns it.
	public String getDescription() {
		return description;
	}
	
	// Setting up a delete function for use in the service file.
	public Task deleteTask(Task deleteTask) {
		deleteTask.taskId = null;
		deleteTask.name = null;
		deleteTask.description = null;
		deleteTask = null;
		return deleteTask;
	}
}
```

### TaskTest.java

```java
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class TaskTest {

	
	// Checks if the task class works correctly with correct input.
	@Test
	void taskTestAllCorrect() {
		Task taskTest = new Task("1", "1", "1");
		assertTrue(taskTest.getTaskId().equals("1"));
		assertTrue(taskTest.getName().equals("1"));
		assertTrue(taskTest.getDescription().equals("1"));
	}
	
	// Id tests.
	
	// Tests if an error is thrown when the id input has too many characters.
	@Test
	void taskTestTooMuchId() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Task taskTest = new Task("11111111111", "1", "1");	
		});
	}
	
	// Tests if an error is thrown when the id input is null
	@Test
	void taskTestIdNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Task taskTest = new Task(null, "1", "1");	
		});
	}
	
	// Name tests.
	
	// Tests if an error is thrown when the name input has too many characters.
	@Test
	void taskTestTooMuchName() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Task taskTest = new Task("1", "toomuchname1111111111", "1");	
		});
	}
	
	// Tests if an error is thrown when the name input is null
	@Test
	void taskTestNameNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Task taskTest = new Task("1", null, "1");	
		});
	}
	
	// Description tests.
	
	// Tests if an error is thrown when the description input has too many characters.
	@Test
	void taskTestTooMuchDescription() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Task taskTest = new Task("1", "1", "toomuch11111111111111111111111111111111111111111111");	
		});
	}
	
	// Tests if an error is thrown when the description input is null
	@Test
	void taskTestDescriptionNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Task taskTest = new Task("1", "1", null);	
		});
	}


}
```

### TaskService.java

```java

public class TaskService {
	
	
	// Stores if the new task has been added updated or deleted successfully.
	static public boolean added = false;
	static public boolean deleted = false;
	static public boolean updated = false;
	
	// TaskService constructor.
	public TaskService (boolean add, boolean delete, boolean update, String newId, String updateName, String updateDescription) {
		
		// Creating task for testing
		Task taskTest = new Task("1", "1111", "1111111111111111111111111");
		
		// Creating placeholder task so that errors do not pop up in delete area.
		Task newTask = new Task (" ", " ", " ");
		
		// Checks if add input is true, then creates a new task.
		if (add == true && newId != "1") {
			newTask = new Task(newId, updateName, updateDescription);
			added = true;
		}
		
		// Tells user that the id they wanted to add was already used.
		else if (add == true) {
			throw new IllegalArgumentException("Already have task with that Id.");
		}
		
		// Checks if delete is true and the id is valid, then deletes the correct task.
		if (delete == true && (newId == "1" || add == true)) {
		
			// Deletes and checks if the task was deleted successfully.
			try {
				if (delete == true) {
					newTask = newTask.deleteTask(newTask);
				}
				else {
					taskTest = taskTest.deleteTask(taskTest);
				}
				
				// Updates deleted to show that the task was deleted.
				if (taskTest == null || newTask == null) {
					deleted = true;
				}
			
			}
			
			// Updates deleted to show that the task was deleted.
			catch (NullPointerException e) {
				deleted = true;
			}
		}
		
		// Tells user that the id they input is not valid to delete
		else if (delete == true) {
			throw new IllegalArgumentException("Cannot delete task, id invalid.");
		}
		
		// Checks if user wants to update an existing task, does it if they do.
		if (update == true && newId == "1") {
			taskTest.setDescription(updateDescription);
			taskTest.setName(updateName);
			
			// Shows update happened
			updated = true;
		}
		
		// Tells the user that the id they input did not have a task connected to it.
		else if (update == true) {
			throw new IllegalArgumentException("Cannot update task, no task with same id");
		}
	}
}
```
### TaskServiceTest.java

```java
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class TaskServiceTest {

	// Add, delete, and update functions work correctly.
	
	// Add test works correctly.
	@Test
	void addTestCorrect() {
		new TaskService(true, false, false, "2", "2", "2");
		assertTrue(TaskService.added);
	}
	
	// Delete test works correctly.
	@Test
	void deleteTestCorrect() {
		new TaskService(false, true, false, "1", null, null);
		assertTrue(TaskService.deleted);
	}
	
	// Update test works correctly.
	@Test
	void updateTestCorrect() {
		new TaskService(false, false, true, "1", "new", "new");
		assertTrue(TaskService.updated);
	}
	
	// Tests if functions do not work when given incorrect input.
	
	// Add test does not work when given the same id as an existing task.
	@Test
	void addTestIncorrectId() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new TaskService(true, false, false, "1", "new", "new");
			});
	}
	
	// Delete test does not work when given the wrong id.
	@Test
	void deleteTestIncorrectId() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new TaskService(false, true, false, "2", null, null);
			});
	}
	
	// Update test  does not work when given the wrong id.
	@Test
	void updateTestIncorrectId() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new TaskService(false, false, true, "2", "new", "new");
			});
	}
	


}
```

# New Artifact:
## Appointment Service

### Appointment.py

```python
import datetime

# Declaring variables, removing magic numbers
APPOINTMENTIDMAX = 10
APPOINTMENTDESCRIPTIONMAX = 50


class Appointment:

    # Citation for self usage: (Gyanendra371, 2024)

    # (Erakshaya485, 2024), initializing appointment object
    def __init__(self, newAppointmentId, newAppointmentDate, newAppointmentDescription, newAppointmentInstantce): 
        if newAppointmentInstantce == True:
            return
        
        self.Appointment(newAppointmentId, newAppointmentDate, newAppointmentDescription)

    def Appointment(self, newAppointmentId, newAppointmentDate, newAppointmentDescription):


        # (TonyA, 2013; Rollbar Editorial Team, 2023), appointment id being set, and error checking.
        try:
            if len(newAppointmentId) <= APPOINTMENTIDMAX:
                self.addedCorrectly = True
                self.appointmentId = newAppointmentId

            # Too Long of id
            elif len(newAppointmentId) > APPOINTMENTIDMAX:
                print("Appointment id is too long, please keep it to 10 characters or less.")
                raise Exception
            
            # Null Id
            elif newAppointmentId == None:
                print("Appointment id is null, please enter an id.")
                raise Exception
            
        except:
             self.addedCorrectly = False
        
        # Calls functions to set input other information.
        self.setAppointmentDate(newAppointmentDate)
        self.setAppointmentDescription(newAppointmentDescription)

        # Returns object
        return self



    # Setters and getters
    def getAppointmentId(self):
          return self.appointmentId
    
    def getAppointmentDate(self):
          return self.appointmentDate
    
    def setAppointmentDate(self, newAppointmentDate):

        # Gets the current time for later comparison.
        dateToday = datetime.date.today()
        
        # (TonyA, 2013; Rollbar Editorial Team, 2023), Sets appointment date if is valid.
        try:
            if newAppointmentDate > dateToday:
                self.appointmentDate = newAppointmentDate
            
            # Date in past
            elif newAppointmentDate < dateToday:
                print("Appointment date is before the current date, please enter a valid date.")
                raise Exception
            
            # Null date input
            elif newAppointmentDate == None:
                print("Appointment date is null, please enter a date.")
                raise Exception
        except:
             self.addedCorrectly = False # Flags incorrect data
                
            

    def getAppointmentDescription(self):
          return self.appointmentDescription
    
    def setAppointmentDescription(self, newAppointmentDescription):

        # (TonyA, 2013; Rollbar Editorial Team, 2023), Appointment description being set as well as error checking.
        try:
            if len(newAppointmentDescription) <= APPOINTMENTDESCRIPTIONMAX:
                self.appointmentDescription = newAppointmentDescription

            # Description too long
            elif len(newAppointmentDescription) > APPOINTMENTDESCRIPTIONMAX:
                print("Appointment description is too long, please keep it to 50 characters or less.")
                raise Exception
            
            # Null description input
            elif newAppointmentDescription.equals(None):
                print(("Appointment description is null, please enter an description."))
                raise Exception
        except:
            self.addedCorrectly = False # Flags incorrect data
    
    # Function deletes information stored within object
    def deleteAppointmentInfo(self):
          self.appointmentId = None
          self.appointmentDate = None
          self.appointmentDescription = None
```

### AppointmentTest.py

```python
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
```

### AppointmentService.py

```python
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
                if newAppointment.addedCorrectly == False:
                    self.added = False
                    return
                else:
                    self.added = True
                    return newAppointment
        
        # User incorrect id error check
            elif (addAppointment == True) and (appointmentExists == True):
                raise Exception
        except:
            self.added = False
            print("Appointment with input id has already been made, please use another id.")

        
    # Deletes an appointment.
    def deletingAppointment(self, deleteAppointment, appointmentExists, appointmentList, appointmentId): 
        
        # Variable to iterate through appointment list to find location of same appointment
        sameAppointmentId = 0

        # (TonyA, 2013; Rollbar Editorial Team, 2023), deleting appointment with error checking
        try:
            if (deleteAppointment == True) and (appointmentExists == True):
                for incrementAppointmentList in appointmentList:
                    if appointmentId == incrementAppointmentList.getAppointmentId():
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
                self.deleted = False
                print("Appointment with input id does not exist, can not delete.")
```

### AppointmentServiceTest.py

```python
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
```


## Contact Service

### Contact.py </summary>

```python
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
```

### ContactTest.py

```python
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
```

### ContactService.py 

```python
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
```

### ContactServiceTest.py

```python
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
```

## Task Service

### Task.py

```python
import datetime

# Declaring variables, removing magic numbers
TASKIDMAX = 10
TASKDESCRIPTIONMAX = 50

class Task:

    # Citation for self usage: (Gyanendra371, 2024)

    # (Erakshaya485, 2024), initializing task object
    def __init__(self, newTaskId, newTaskDate, newTaskDescription, newTaskInstantce): 
        if newTaskInstantce == True:
            return
        
        self.Task(newTaskId, newTaskDate, newTaskDescription)

    def Task(self, newTaskId, newTaskDate, newTaskDescription):


        # (TonyA, 2013; Rollbar Editorial Team, 2023), task id being set, and error checking.
        try:
            if len(newTaskId) <= TASKIDMAX:
                self.addedCorrectly = True
                self.taskId = newTaskId

            # Too Long of id
            elif len(newTaskId) > TASKIDMAX:
                print("Task id is too long, please keep it to 10 characters or less.")
                raise Exception
            
            # Null Id
            elif newTaskId == None:
                print("Task id is null, please enter an id.")
                raise Exception
            
        except:
             self.addedCorrectly = False
             return self
        
        # Calls functions to set input other information.
        self.setTaskDate(newTaskDate)
        self.setTaskDescription(newTaskDescription)

        # Returns object
        return self



    # Setters and getters
    def getTaskId(self):
          return self.taskId
    
    def getTaskDate(self):
          return self.taskDate
    
    def setTaskDate(self, newTaskDate):

        # Gets the current time for later comparison.
        dateToday = datetime.date.today()
        
        # (TonyA, 2013; Rollbar Editorial Team, 2023), Sets task date if is valid.
        try:
            if newTaskDate > dateToday:
                self.taskDate = newTaskDate
            
            # Date in past
            elif newTaskDate < dateToday:
                print("Task date is before the current date, please enter a valid date.")
                raise Exception
            
            # Null date input
            elif newTaskDate == None:
                print("Task date is null, please enter a date.")
                raise Exception
        except:
             self.addedCorrectly = False # Flags incorrect data
                
            

    def getTaskDescription(self):
          return self.taskDescription
    
    def setTaskDescription(self, newTaskDescription):

        # (TonyA, 2013; Rollbar Editorial Team, 2023), task description being set as well as error checking.
        try:
            if len(newTaskDescription) <= TASKDESCRIPTIONMAX:
                self.taskDescription = newTaskDescription

            # Description too long
            elif len(newTaskDescription) > TASKDESCRIPTIONMAX:
                print("Task description is too long, please keep it to 50 characters or less.")
                raise Exception
            
            # Null description input
            elif newTaskDescription.equals(None):
                print(("Task description is null, please enter an description."))
                raise Exception
        except:
            self.addedCorrectly = False # Flags incorrect data
    
    # Function deletes information stored within object
    def deleteTaskInfo(self):
          self.taskId = None
          self.taskDate = None
          self.taskDescription = None
    
    # Function updates information within object.
    def updateTaskInfo(self, newTaskDate, newTaskDescription):
        self.taskDate = self.setTaskDate(newTaskDate)
        self.taskDescription = self.setTaskDescription(newTaskDescription)
```

### TaskTest.py
```python
import unittest
from Task import Task
import datetime

class TaskTests (unittest.TestCase):

    # Test with all information correct
    def testTaskAllCorrect(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)
        checkTask.Task("1", datetime.date(2025, 1, 1), "1")
    
        # Checks Task information
        self.assertEqual(checkTask.getTaskId(), "1")
        self.assertEqual(checkTask.getTaskDate(), datetime.date(2025, 1, 1))
        self.assertEqual(checkTask.getTaskDescription(), "1")
        self.assertTrue(checkTask.addedCorrectly)


    # Task id tests
    def testTaskIdLong(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)

        # Checks if Task was not added
        self.assertFalse(checkTask.Task("11111111111", datetime.date(2025, 1, 1), "1").addedCorrectly)


    def testTaskIdNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)

        # Checks if Task was not added
        self.assertFalse(checkTask.Task(None, datetime.date(2025, 1, 1), "1").addedCorrectly)


    # Task date tests
    def testTaskDateBeforeCurrent(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)

        # Checks if Task was not added
        self.assertFalse(checkTask.Task("1", datetime.date(2023, 1, 1), "1").addedCorrectly)


    def testTaskDateNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)

        # Checks if Task was not added
        self.assertFalse(checkTask.Task("1", None, "1").addedCorrectly)


    # Task description test
    def testTaskDescriptionLong(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)

        # Checks for addition of Task
        self.assertFalse(checkTask.Task("1", datetime.date(2025, 1, 1), (51 * "1")).addedCorrectly)


    def testTaskDescriptionNull(self):

        # (Kalra, 2023; Everythingtech, 2023), initialises Task
        checkTask = Task(None, None, None, True)

       # Checks for addition of Task
        self.assertFalse(checkTask.Task("1", datetime.date(2025, 1, 1), None).addedCorrectly)
 
        
# Calls the unit tests
if __name__== '__main__':
    unittest.main()
```

### TaskService.py

```python
from Task import Task

# Declaring variables, removing magic numbers
STORESTASK = 1

class TaskService:

    # Citation for self usage: (Gyanendra371, 2024)

    # (Erakshaya485, 2024), initializes the class.
    def __init__(self, addTask, deleteTask, updateTask, taskList, taskId, taskDate, taskDescription):
        if addTask == None:
            return
        
        self.TaskService(addTask, deleteTask, updateTask, taskList, taskId, taskDate, taskDescription)

    # Main task service function
    def TaskService(self, addTask, deleteTask, updateTask, taskList, taskId, taskDate, taskDescription):

        self.added = False
        self.deleted = False
        self.updated = False
        taskExists = False

        if len(taskList) >= STORESTASK:

            # Checks if an task already exists with input id.
            for incrementTaskList in taskList:
                if taskId == incrementTaskList.getTaskId():
                    taskExists = True
        
                else:
                    taskExists = False
        
        # Adding task
        if addTask == True:
            confirmationTask = self.addingTask(addTask, taskExists, taskId, taskDate, taskDescription)

            return confirmationTask

        # Deleting task
        if deleteTask == True:
            self.deletingTask(deleteTask, taskExists, taskList, taskId)

        # Updating task
        if updateTask == True:
            self.updatingTask(updateTask, taskExists, taskList, taskId, taskDate, taskDescription)
                


    # Adds an task
    def addingTask(self, addTask, taskExists, taskId, taskDate, taskDescription): 
        
        # (Kalra, 2023; Everythingtech, 2023), initializing new task
        newTask = Task(None, None, None, True)

        # (TonyA, 2013; Rollbar Editorial Team, 2023), adding task with error checking
        try:
            if (addTask == True) and (taskExists == False):
                newTask.Task(taskId, taskDate, taskDescription)
                if newTask.addedCorrectly == False:
                    self.added = False
                    return
                else:
                    self.added = True
                    return newTask
        
        # User incorrect id error check
            elif (addTask == True) and (taskExists == True):
                raise Exception
        except:
            self.added = False
            print("Task with input id has already been made, please use another id.")

        
    # Deletes a task.
    def deletingTask(self, deleteTask, taskExists, taskList, taskId): 
        
        # Variable to iterate through task list to find location of same task
        sameTaskId = 0
        # (TonyA, 2013; Rollbar Editorial Team, 2023), deleting task with error checking
        try:
            if (deleteTask == True) and (taskExists == True):
                for incrementTaskList in taskList:
                    if taskId == incrementTaskList.getTaskId():
                        taskDelete = taskList.pop(sameTaskId)
                        taskDelete.deleteTaskInfo()
                        taskDelete = None
                        self.deleted = True
                
                    # Adds one after if statment since the list can store at [0]
                    sameTaskId += 1

            # User inccorect id error check
            elif (deleteTask == True) and (taskExists == False):
                raise Exception
        except:
                self.deleted = False
                print("Task with input id does not exist, can not delete.")

    # Updates a task.
    def updatingTask(self, updateTask, taskExists, taskList, taskId, taskDate, taskDescription): 
        
        # Variable to iterate through task list to find location of same task
        sameTaskId = 0

        # (TonyA, 2013; Rollbar Editorial Team, 2023), deleting task with error checking
        try:
            if (updateTask == True) and (taskExists == True):
                for incrementTaskList in taskList:
                    if taskId == incrementTaskList.getTaskId():
                        taskUpdate = taskList.pop(sameTaskId)
                        taskUpdate.updateTaskInfo(taskDate, taskDescription)
                        self.updated = True
                
                    # Adds one after if statment since the list can store at [0]
                    sameTaskId += 1

            # User inccorect id error check
            elif (updateTask == True) and (taskExists == False):
                raise Exception
        except:
                self.updated = False
                print("Task with input id does not exist, can not update.")
```

### TaskServiceTest.py

```python
import unittest
from Task import Task
from TaskService import TaskService
import datetime

class TaskTests (unittest.TestCase):

    # Task Service add tests
    def testTaskServiceAddCorrect(self):
        
        # Initializing empty list for test
        checkTaskList = []

        # # (Kalra, 2023; Everythingtech, 2023), initializing and entering correct info into the Task service
        checkTaskServices = TaskService(None, None, None, None, None, None, None)
        checkTaskServices.TaskService(True, False, False, checkTaskList, "1", datetime.date(2025, 1, 1), "1")
        
        # Checks added variable to see if addition happened
        self.assertEqual(checkTaskServices.added, True)
    
    def testTaskServiceAddIdIncorrect(self):
        
        # Creating Task test list
        checkTaskList = []

        # (Kalra, 2023; Everythingtech, 2023), creates an existing Task and stores it
        checkTask = Task(None, None, None, True)
        checkTask.Task("1", datetime.date(2025, 1, 1), "1")
        checkTaskList.append(checkTask) 

        # Initializes Task services
        checkTaskServices = TaskService(None, None, None, checkTaskList, None, None, None)
        
        # Inputs incorrect addition information into Task services
        checkTaskServices.TaskService(True, False, False, checkTaskList, "1", datetime.date(2025, 1, 1), "1")
        
        # Checks added variable to see if addition happened
        self.assertFalse(checkTaskServices.added)

    
    # Delete tests
    def testTaskServiceDeleteCorrect(self):
        
        # Creating Task test list
        checkTaskList = []

        # (Kalra, 2023; Everythingtech, 2023), creates an existing Task and stores it
        checkTask = Task(None, None, None, True)
        checkTask.Task("1", datetime.date(2025, 1, 1), "1")
        checkTaskList.append(checkTask) 

        # Initializes Task services and inputs correct deletion information
        checkTaskServices = TaskService(None, None, None, checkTaskList, None, None, None)
        checkTaskServices.TaskService(False, True, False, checkTaskList, "1", datetime.date(2025, 1, 1), "1")
        
        # Checks added variable to see if deletion happened
        self.assertEqual(checkTaskServices.deleted, True)

    def testTaskServiceDeleteIdIncorrect(self):
        
        # Creating Task test list
        checkTaskList = []

        # (Kalra, 2023; Everythingtech, 2023), initializes Task services
        checkTaskServices = TaskService(None, None, None, checkTaskList, None, None, None)
        
        # Inputs incorrect deletion information and checks for non-deletion
        checkTaskServices.TaskService(False, True, False, checkTaskList, "2", None, None)
        self.assertFalse(checkTaskServices.deleted)


    # Update tests
    def testTaskServiceUpdateCorrect(self):
        
        # Creating Task test list
        checkTaskList = []

        # (Kalra, 2023; Everythingtech, 2023), creates an existing Task and stores it
        checkTask = Task(None, None, None, True)
        checkTask.Task("1", datetime.date(2025, 1, 1), "1")
        checkTaskList.append(checkTask) 

        # Initializes Task services and inputs correct deletion information
        checkTaskServices = TaskService(None, None, None, checkTaskList, None, None, None)
        checkTaskServices.TaskService(False, False, True, checkTaskList, "1", datetime.date (2026, 1, 1), "2")
        
        # Checks added variable to see if deletion happened
        self.assertEqual(checkTaskServices.updated, True)

    def testTaskServiceUpdateIdIncorrect(self):
        
        # Creating Task test list
        checkTaskList = []

        # (Kalra, 2023; Everythingtech, 2023), initializes Task services
        checkTaskServices = TaskService(None, None, None, checkTaskList, None, None, None)
        
        # Inputs incorrect update.
        checkTaskServices.TaskService(False, False, True, checkTaskList, "2", None, None)
        self.assertFalse(checkTaskServices.updated)

# Starts unit tests        
if __name__== '__main__':
    unittest.main()
```

