
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
