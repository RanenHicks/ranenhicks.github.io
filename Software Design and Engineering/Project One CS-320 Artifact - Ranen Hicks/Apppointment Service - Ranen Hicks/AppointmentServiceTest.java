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
