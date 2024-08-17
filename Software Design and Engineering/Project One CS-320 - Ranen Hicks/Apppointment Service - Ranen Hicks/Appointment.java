
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
