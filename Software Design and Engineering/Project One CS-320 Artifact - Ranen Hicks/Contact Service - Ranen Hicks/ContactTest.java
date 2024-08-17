import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class ContactTest {

	@Test
	void testAllCorrect() {
		
		// Checks if the contact class works correctly with correct input
		Contact contact = new Contact("209", "11", "11", "1111111111", "1111");
		assertTrue(contact.getContactId().equals("209"));
		assertTrue(contact.getFirstName().equals("11"));
		assertTrue(contact.getLastName().equals("11"));
		assertTrue(contact.getPhone().equals("1111111111"));
		assertTrue(contact.getAddress().equals("1111"));
	}
	
	// Id
	
	@Test
	void testIdIncorretTooMany() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("toomanyvals", "11", "11", "1111111111", "1111");
		});
	}
	@Test
	void testIdIncorretNull() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact(null, "11", "11", "1111111111", "1111");
		});
	}
	
	// First Name
	@Test
	void testFirstNameIncorretTooMany() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "toomanyvals", "11", "1111111111", "1111");
		});
	}
	
	@Test
	void testFirstNameIncorretNull() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", null, "11", "1111111111", "1111");
		});
	}
	
	//Last Name
	
	@Test
	void testLastNameIncorretTooMany() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", "toomanyvals", "1111111111", "1111");
		});
	}
	
	@Test
	void testLastNameIncorretNull() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", null, "1111111111", "1111");
		});
	}
	
	//Phone
	@Test
	void testPhoneIncorrectNotNumbers() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", "11", "1111111hi1", "1111");
		});	
	}
	
	@Test
	void testPhoneIncorretNull() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", "11", null, "1111");
		});
	}
	
	@Test
	void testPhoneIncorrectTooMany() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", "11", "11111111111", "1111");
		});
	}
	
	// Address
	
	@Test
	void testAddressncorretTooMany() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", "11", "1111111111", "toomanyvals11111111111111111111");
		});
	}
	
	@Test
	void testAddressIncorretNull() {
		
		// Checks if the phone exception works.
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			Contact contact = new Contact("209", "11", "11", "1111111111", null);
		});
	}
}
