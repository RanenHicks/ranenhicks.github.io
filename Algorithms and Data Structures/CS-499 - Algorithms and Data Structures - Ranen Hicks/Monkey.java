
/*
 * This program allows the user to add dogs and monkeys into their respective lists, reserve an animal, print out the dogs in their list, print out the monkeys in their
 * list, or print out the animals that are available. These things can be done multiple times until the user specifies the program to stop by entering q.
 * 
 * Author: Ranen Hicks
 * Date: December 10, 2022
*/
public class Monkey extends RescueAnimal {

	// Declaring all new private variables for the monkey class.
	private String mTailLength;
	private String mHeight;
	private String mBodyLength;
	private String mSpecies;
	
	// Constructor sets all the variables that the monkey object will have to the user's input.
	public Monkey(String mName, String mGender, int mAge, String mWeight, String mAcquisitionDate, String mAcquisitionCountry, boolean mReserved, 
	       String mInServiceCountry, String mTrainingStatus, String mTailLength, String mHeight, String mBodyLength, String mSpecies) {
		
		// Uses methods from the RescueAnimal class.
		setName(mName);
		setGender(mGender);
		setAge(mAge);
		setWeight(mWeight);
		setAcquisitionDate(mAcquisitionDate);
		setAcquisitionLocation(mAcquisitionCountry);
		setReserved(mReserved);
		setInServiceCountry(mInServiceCountry);
		setTrainingStatus(mTrainingStatus);
		
		// Methods in this Monkey class.
		setMonkeyTailLength(mTailLength);
		setMonkeyHeight(mHeight);
		setMonkeyBodyLength(mBodyLength);
		setMonkeySpecies(mSpecies);
	}
	
	// Setters and getters 
	public String getMonkeyTailLength() {
		return mTailLength;
	}
	
	// Sets the tail length of the monkey to the input.
	public void setMonkeyTailLength(String inputTailLength) {
		mTailLength = inputTailLength;
	}
	
	// Grabs the height of the monkey for use in other parts of code.
	public String getMonkeyHeight() {
		return mHeight;
	}
	
	// Sets the height to the user input.
	public void setMonkeyHeight(String inputHeight) {
		mHeight = inputHeight;
	}
	
	// Gets the body length and returns it to be used elsewhere.
	public String getMonkeyBodyLength() {
		return mBodyLength;
	}
	
	// Body length of monkey is set to the user's input.
	public void setMonkeyBodyLength(String inputBodyLength) {
		mBodyLength = inputBodyLength;
	}
	
	// Returns the species of the monkey to where it is needed.
	public String getMonkeySpecies() {
		return mSpecies;
	}
	
	// The species of the monkey is saved as the user's input.
	public void setMonkeySpecies(String inputSpecies) {
		mSpecies = inputSpecies;
	}
}