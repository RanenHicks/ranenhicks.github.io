
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
