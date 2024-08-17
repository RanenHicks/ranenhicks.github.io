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
