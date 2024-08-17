
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
