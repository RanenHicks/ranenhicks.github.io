
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
	public Monkey(String mName, String mGender, String mAge, String mWeight, String mAcquisitionDate, String mAcquisitionCountry, boolean mReserved, 
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
		setTailLength(mTailLength);
		setHeight(mHeight);
		setBodyLength(mBodyLength);
		setSpecies(mSpecies);
	}
	
	// Returns tail length to where method is called.
	public String getTailLength() {
		return mTailLength;
	}
	
	// Sets the tail length of the monkey to the input.
	public void setTailLength(String inputTailLength) {
		mTailLength = inputTailLength;
	}
	
	// Grabs the height of the monkey for use in other parts of code.
	public String getHeight() {
		return mHeight;
	}
	
	// Sets the height to the user input.
	public void setHeight(String inputHeight) {
		mHeight = inputHeight;
	}
	
	// Gets the body length and returns it to be used elsewhere.
	public String getBodyLength() {
		return mBodyLength;
	}
	
	// Body length of monkey is set to the user's input.
	public void setBodyLength(String inputBodyLength) {
		mBodyLength = inputBodyLength;
	}
	
	// Returns the species of the monkey to where it is needed.
	public String getSpecies() {
		return mSpecies;
	}
	
	// The species of the monkey is saved as the user's input.
	public void setSpecies(String inputSpecies) {
		mSpecies = inputSpecies;
	}
}
