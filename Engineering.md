<<!-- (Github basic writing and formatting syntax, n.d.; pierrejoubert73, 2024) -->>
# Software Development and Engineering
## Old Artifact:

### Appointment Services:
<details>
  <summary> Appointment.java </summary>
  
	```Java
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
</details>
<details>
  <summary> ContactTest.java </summary>
</details>
<details>
  <summary> ContactService.java </summary>
</details>
<details>
  <summary> ContactServiceTest.java </summary>
</details>
### Task Services:
<details>
  <summary> Task.java </summary>
</details>
<details>
  <summary> TaskTest.java </summary>
</details>
<details>
  <summary> TaskService.java </summary>
</details>
<details>
  <summary> TaskServiceTest.java </summary>
</details>
