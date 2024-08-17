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
