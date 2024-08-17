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
