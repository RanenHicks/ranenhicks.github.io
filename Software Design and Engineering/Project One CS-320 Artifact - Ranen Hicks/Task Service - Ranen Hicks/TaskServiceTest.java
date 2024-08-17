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
