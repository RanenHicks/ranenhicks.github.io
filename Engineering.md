<!-- (Github basic writing and formatting syntax, n.d.; pierrejoubert73, 2024) -->
# Software Development and Engineering
## [See the Artifacts in the Repository](https://github.com/RanenHicks/ranenhicks.github.io/tree/main/Software%20Design%20and%20Engineering)

## Old Artifact:

### Appointment Services:
<details>
  <summary> Appointment.java </summary>
	
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
</details>
<details>
  <summary> AppointmentTest.java </summary>

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
</details>
<details>
  <summary> AppointmentService.java </summary>
  
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
</details>
<details>
  <summary> AppointmentServiceTest.java </summary>

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
</details>

### Contact Services:
<details>
  <summary> Contact.java </summary>

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
</details>
<details>
  <summary> ContactTest.java </summary>

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
</details>
<details>
  <summary> ContactService.java </summary>

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
</details>
<details>
  <summary> ContactServiceTest.java </summary>

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
</details>

### Task Services:
<details>
  <summary> Task.java </summary>

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
</details>
<details>
  <summary> TaskTest.java </summary>

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
</details>
<details>
  <summary> TaskService.java </summary>

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
</details>
<details>
  <summary> TaskServiceTest.java </summary>

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
</details>

## New Artifact:
