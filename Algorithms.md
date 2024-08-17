<!-- (Adding content to your GitHub Pages site using Jekyll, n.d.) -->
[Go Back](README.md)

# Algorithms and Data Structures

## [See the Code in the Repository](Algorithms and Data Structures)

## Click to Navigate:
### [Old Artifact (IT-145 Artifact Without Enchancements)](#old-artifact)
### [New Artifact (CS-499 Algorithms and Data Structures Enhancement)](#new-artifact)

# Old Artifact:
### Driver.java
```java
import java.util.ArrayList;
import java.util.Scanner;

// Importing error checking.
import java.util.InputMismatchException;

public class Driver {
    private static ArrayList<Dog> dogList = new ArrayList<Dog>();
    
    //Declaring and creating new list for monkeys.
    private static ArrayList<Monkey> monkeyList = new ArrayList<Monkey>();

    public static void main(String[] args) {
    
    	String userInput;
    	int printList = 0;
    	int i = 0;
    	
    	Scanner scnr = new Scanner(System.in);

        initializeDogList();
        initializeMonkeyList();
        
        // Displays the menu until q is entered.
        while (i != -1) {
        	displayMenu();
        	userInput = scnr.nextLine();
        	switch (userInput) {
        	
        	    // When q is input, the loop will stop.
        	    case "q":
        		    i = -1; // Stops the loop.
        		    break;
        		
        		// Takes user to the method to input new dog into list.
        	    case "1":
        		    intakeNewDog(scnr);
        		    break;
        	
        		// Takes user to method to input new monkey.
        	    case "2":
        		    intakeNewMonkey(scnr);
        		    break;
        		
        		// Takes user to the method to reserve an animal.
        	    case "3":
        		    reserveAnimal(scnr);
        		    break;
        	
        		// Prints out the dogs in the dog list.
        	    case "4":
        	    	printList = 4;
        		    printAnimals(printList);
        		    break;
        		
        		// Prints out the monkeys in the monkey list.
        	    case "5":
        	    	printList = 5;
        		    printAnimals(printList);
        		    break;
        	
        		// Prints out the available animals.
        	    case "6":
        	    	printList = 6;
        		    printAnimals(printList);
        		    break;
        	
        		// If none of the other cases work, then user input is incorrect and the user is told such.
        	    default:
        			System.out.print("Incorrect input. Please try Again.\n");
        			break;
        	}
        }
        

    }

    public static void displayMenu() {
        System.out.println("\n\n");
        System.out.println("\t\t\t\tRescue Animal System Menu");
        System.out.println("[1] Intake a new dog");
        System.out.println("[2] Intake a new monkey");
        System.out.println("[3] Reserve an animal");
        System.out.println("[4] Print a list of all dogs");
        System.out.println("[5] Print a list of all monkeys");
        System.out.println("[6] Print a list of all animals that are not reserved");
        System.out.println("[q] Quit application");
        System.out.println();
        System.out.println("Enter a menu selection");
    }


    public static void initializeDogList() {
        Dog dog1 = new Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "intake", false, "United States");
        Dog dog2 = new Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "Phase I", false, "United States");
        Dog dog3 = new Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", true, "Canada");
        
       // Added to test if option 6 worked.
        Dog dog4 = new Dog("Hello", "Sheltie", "female", "5", "22.4", "1-22-17", "United States", "In Service", false, "United States");

        dogList.add(dog1);
        dogList.add(dog2);
        dogList.add(dog3);
        dogList.add(dog4);
    }

    public static void initializeMonkeyList() {
    	// Adding two monkeys to the list to check for errors.
    	Monkey monkey1 = new Monkey("Test", "TestSpecies", "male", "12", "22.8", "Test", false, "Test", "In Service", "United States", "Test", "Test", "Test");
    	Monkey monkey2 = new Monkey("Testing", "TestSpecies", "female", "12", "22.8", "Test", true, "Test", "In Service", "United States", "Test", "Test", "Test");
    	monkeyList.add(monkey1);
    	monkeyList.add(monkey2);
    }

    public static void intakeNewDog(Scanner scanner) {
    	// Declaring the variables for the new dog object except for name since that is already in the code.
    	String dBreed;
    	String dGender;
    	String dAge;
    	String dWeight;
    	String dAcquisitionDate;
        String dAcquisitionCountry;
        boolean dReserved = false;
	    String dInServiceCountry;
	    String dTrainingStatus;
	    int error = -1;
    	
        System.out.println("What is the dog's name?");
        String name = scanner.nextLine();
        for(Dog dog: dogList) {
            if(dog.getName().equalsIgnoreCase(name)) {
                System.out.println("\n\nThis dog is already in our system\n\n");
                return;
            }
        }
        
        // Grabs the rest of the info needed about the dog from the user.
        System.out.println("What is the dog's breed?");
        dBreed = scanner.nextLine();
    	System.out.println("What is the dog's gender?");
    	dGender = scanner.nextLine();
    	System.out.println("What is the dog's age?");
    	dAge = scanner.nextLine();
    	System.out.println("What is the dog's weight?");
    	dWeight = scanner.nextLine();
    	System.out.println("What is the dog's acquisition date?");
    	dAcquisitionDate = scanner.nextLine();
    	System.out.println("What is the dog's acquisition location?");
    	dAcquisitionCountry = scanner.nextLine();
    	
    	// Checks if the user input the reserved variable wrong.
    	while (error == -1) {
    		error = 0; // Sets error to 0 so that the loop stops if input is correct.
    		
    		// Checks if there is an error with the user's input.
    	    try {
        	    System.out.println("Is the dog reserved?");
        	    dReserved = scanner.nextBoolean();
        	}
    		
    		// If error is found, error will be set back to -1 and the user will be told that they input an error.
        	catch (InputMismatchException e) {
        	error = -1;
        	System.out.println("Error: Please enter a boolean value.\n");
    	    scanner.nextLine(); // Gets to the next line for next input, makes sure that the loop does not go forever.
        	}
    	}
    	
    	scanner.nextLine(); // For next input.
    	
    	// Gets the rest of the information of the dog.
    	System.out.println("What is the dog's in service country?");
    	dInServiceCountry = scanner.nextLine();
    	System.out.println("What is the dog's training status?");
        dTrainingStatus = scanner.nextLine();
        
        // Creates a new dog object and adds that to the dog list.
        Dog dog = new Dog(name, dBreed, dGender, dAge, dWeight, dAcquisitionDate, dAcquisitionCountry, dTrainingStatus, dReserved, dInServiceCountry);
        dogList.add(dog);
        
    }

        public static void intakeNewMonkey(Scanner scanner) {
        	// Declaring all the variables that will be needed to create a new monkey object that will be added to the list.
        	String mName;
        	String mGender;
        	String mAge;
        	String mWeight;
        	String mAcquisitionDate;
            String mAcquisitionCountry;
            boolean mReserved = false;
 	        String mInServiceCountry;
 	        String mTrainingStatus;
 	        String mTailLength;
 	        String mHeight;
 	        String mBodyLength;
 	        String mSpecies;
 	        int error = -1;
        	
        	// Checks if the monkey is already in the list.
 	       System.out.println("What is the monkey's name?");
           mName = scanner.nextLine();
        	for (Monkey monkey: monkeyList) {
        		if (monkey.getName().equalsIgnoreCase(mName)) {
        			System.out.println("This Monkey is already in our system.");
        			return;
        		}
        	}
        	
        	// Checks if the monkey's species is a valid species.
        	System.out.println("What is the monkey's species?");
        	mSpecies = scanner.nextLine();
        	if (mSpecies.equalsIgnoreCase("Capuchin") || mSpecies.equalsIgnoreCase("Guenon") || mSpecies.equalsIgnoreCase("Macaque") || 
            mSpecies.equalsIgnoreCase("Marmoset") || mSpecies.equalsIgnoreCase("Squirrel monkey") || mSpecies.equalsIgnoreCase("Tamarin")) {
        		
        		// The rest of the information that is needed about the monkey is input from the user with their respective prompts.
            	System.out.println("What is the monkey's gender?");
            	mGender = scanner.nextLine();
            	System.out.println("What is the monkey's age?");
            	mAge = scanner.nextLine();
            	System.out.println("What is the monkey's weight?");
            	mWeight = scanner.nextLine();
            	System.out.println("What is the monkey's acquisition date?");
            	mAcquisitionDate = scanner.nextLine();
            	System.out.println("What is the monkey's acquisition location?");
            	mAcquisitionCountry = scanner.nextLine();
            	
            	// Checks if the user input the reserved variable wrong.
            	
            	while (error == -1) {
            		error = 0; // Sets error to 0 so that the loop stops if input is correct.
            		
            		try {
                	    System.out.println("Is the monkey reserved?");
                	    mReserved = scanner.nextBoolean();
                	}
            		
            		// If error is found, error will be set back to -1 and the user will be told that they input an error.
                	catch (InputMismatchException e) {
                	    error = -1;
                    	System.out.println("Error: Please enter a boolean value.\n");
                	    scanner.nextLine(); // Gets rid of last input so it does not loop forever.
                	}
            	}

        	    scanner.nextLine(); // Gets to the next line for next input.
        	    
            	// Gets the rest of the info after the reserve information.
            	System.out.println("What is the monkey's in service country?");
            	mInServiceCountry = scanner.nextLine();
            	System.out.println("What is the monkey's training status?");
                mTrainingStatus = scanner.nextLine();
                System.out.println("What is the monkey's tail length?");
            	mTailLength = scanner.nextLine();
            	System.out.println("What is the monkey's height?");
            	mHeight = scanner.nextLine();
            	System.out.println("What is the monkey's body length?");
            	mBodyLength = scanner.nextLine();
            	
            	// Creates new monkey object and adds it to the list with the information.
            	Monkey monkey = new Monkey(mName, mGender, mAge, mWeight, mAcquisitionDate, mAcquisitionCountry, mReserved, mInServiceCountry, mTrainingStatus,
            	mTailLength, mHeight, mBodyLength, mSpecies);
            	monkeyList.add(monkey);
        	}
        	
        	// If the species can not be entered, the program will output that to the user and return to the menu.
        	else {
        		System.out.println("That species can not be entered.");
        		return;
        	}
            
        }

        public static void reserveAnimal(Scanner scanner) {
        	// Declares variables that will be used later.
        	String animalType;
        	String animalInServiceCountry;
        	
        	// Asks the user what animal type they want and stores the information.
        	System.out.println("Do you want a monkey or a dog?");
        	animalType = scanner.nextLine();
        	
        	// Checks if user wants a dog.
        	if (animalType.equalsIgnoreCase("Dog")) {
        		
        		// Checks if there is a dog in the country available.
        		System.out.println("What is the dog's in service country");
            	animalInServiceCountry = scanner.nextLine();
            	
            	// Checks if there is a dog in the list that can be reserved.
            	for (Dog dog: dogList) {
            		if (dog.getInServiceLocation().equalsIgnoreCase(animalInServiceCountry) && dog.getTrainingStatus().equalsIgnoreCase("In Service") && 
            		dog.getReserved() == false) {
            		
            			dog.setReserved(true); // Sets the dog's reserved status to true.
            			System.out.println("Dog has been reserved."); // Tells user dog has been reserved.
            			return; // Stops the for loop so multiple dogs can not be reserved.
            		}
            	}
            	
            	// Tells the user that there is not a dog that can be reserved.
    			System.out.println("There is not a dog that can be reserved in this location.");
        	}
        	
        	// Checks if the user wants a monkey.
        	else if (animalType.equalsIgnoreCase("Monkey")) {
        		
        		// Asks and grabs the user's information about the monkey's service country.
        		System.out.println("What is the monkey's in service country?");
            	animalInServiceCountry = scanner.nextLine();
            	
            	// Checks if a monkey in the list fits the user's wants and reserves the monkey.
            	for (Monkey monkey: monkeyList) {
            		if (monkey.getInServiceLocation().equalsIgnoreCase(animalInServiceCountry) && monkey.getTrainingStatus().equalsIgnoreCase("In Service") && 
            		monkey.getReserved() == false) {
            			monkey.setReserved(true);
            			System.out.println("Monkey has been reserved."); // Tells user that a monkey has been reserved.
            			return; // Stops at first monkey in the list that can be reserved at this location.
            		}
            	}
            	
            	// Prints out that there is not a monkey that can be reserved to the user.
    			System.out.println("There is not a monkey that can be reserved in this location.");
        	}
        	
        	// Tells the user that that animal type is not here.
        	else {
        		System.out.println("We do not have that animal type here.");
        	}
        	
        }
       
        // I added the integer printList here to figure out which list needed to be printed. 
        public static void printAnimals(int printList) {
        	// Switch statement to print out the right list.
        	switch (printList) {
        	
        	    // Would print out the dogs in the list but it is not implemented.
        	    case 4:
        	    	System.out.println("Print dogs in the list.");
        	    	break;
        	    
        	    // Not implemented but would print out the monkeys in the list.
        	    case 5:
        	    	System.out.println("Print monkeys in the list.");
        	    	break;
        	    	
        	    // Prints out the dogs and the monkeys that are available and are trained to the user.
        	    case 6:
        	    	System.out.println("DOGS:"); // Prints out DOGS to make this more readable.
        	    	
        	    	// Checks if the dogs is trained and if it is not reserved for every dog in the list and prints out the dog if it is.
        	    	for (Dog dog: dogList) {
        	    		if(dog.getTrainingStatus().equalsIgnoreCase("In Service") && dog.getReserved() == false) {
        	    			System.out.println(dog.getName() + ", " + dog.getTrainingStatus() + ", " + dog.getAcquisitionLocation() + ", " + "Not Reserved.");
        	    		}
        	    	}
        	    	System.out.println("\n"); // Prints out newline to make it more readable.
        	    	
        	    	System.out.println("MONKEYS:"); // Prints out MONKEYS to split apart the lists.
        	    	
        	    	// Checks if each monkey in the list is trained and is not reserved, and when a monkey is both, it is printed out to the user.
        	    	for (Monkey monkey: monkeyList) {
        	    		if (monkey.getTrainingStatus().equalsIgnoreCase("In Service") && monkey.getReserved() == false) {
        	    			System.out.println(monkey.getName() + ", " + monkey.getTrainingStatus() + ", " + monkey.getAcquisitionLocation() + ", " + "Not Reserved.");
        	    		}
        	    	}
        	    	break;
        	}
        }
}
```

### RescueAnimal.java
```java


import java.lang.String;

public class RescueAnimal {

    // Instance variables
    private String name;
    private String animalType;
    private String gender;
    private String age;
    private String weight;
    private String acquisitionDate;
    private String acquisitionCountry;
	private String trainingStatus;
    private boolean reserved;
	private String inServiceCountry;


    // Constructor
    public RescueAnimal() {
    }


	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}


	public String getAnimalType() {
		return animalType;
	}


	public void setAnimalType(String animalType) {
		this.animalType = animalType;
	}


	public String getGender() {
		return gender;
	}


	public void setGender(String gender) {
		this.gender = gender;
	}


	public String getAge() {
		return age;
	}


	public void setAge(String age) {
		this.age = age;
	}


	public String getWeight() {
		return weight;
	}


	public void setWeight(String weight) {
		this.weight = weight;
	}


	public String getAcquisitionDate() {
		return acquisitionDate;
	}


	public void setAcquisitionDate(String acquisitionDate) {
		this.acquisitionDate = acquisitionDate;
	}


	public String getAcquisitionLocation() {
		return acquisitionCountry;
	}


	public void setAcquisitionLocation(String acquisitionCountry) {
		this.acquisitionCountry = acquisitionCountry;
	}


	public boolean getReserved() {
		return reserved;
	}


	public void setReserved(boolean reserved) {
		this.reserved = reserved;
	}


	public String getInServiceLocation() {
		return inServiceCountry;
	}


	public void setInServiceCountry(String inServiceCountry) {
		this.inServiceCountry = inServiceCountry;
	}




	public String getTrainingStatus() {
		return trainingStatus;
	}


	public void setTrainingStatus(String trainingStatus) {
		this.trainingStatus = trainingStatus;
	}
}
```

### Dog.java
```java

public class Dog extends RescueAnimal {

    // Instance variable
    private String breed;

    // Constructor
    public Dog(String name, String breed, String gender, String age,
    String weight, String acquisitionDate, String acquisitionCountry,
	String trainingStatus, boolean reserved, String inServiceCountry) {
        setName(name);
        setBreed(breed);
        setGender(gender);
        setAge(age);
        setWeight(weight);
        setAcquisitionDate(acquisitionDate);
        setAcquisitionLocation(acquisitionCountry);
        setTrainingStatus(trainingStatus);
        setReserved(reserved);
        setInServiceCountry(inServiceCountry);

    }

    // Accessor Method
    public String getBreed() {
        return breed;
    }

    // Mutator Method
    public void setBreed(String dogBreed) {
        breed = dogBreed;
    }

}
```

### Monkey.java
```java

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
```

# New Artifact:

### Driver.java
```java
/*
 * Author: Ranen Hicks
 * Description: This program simulates a rescue animal center, allowing the user to add, see, and reserve animals. The specific animals in this program currently consist of
 * monkeys and dogs.
 * 
 * References:
 * 
 * barykrg. (2019, January 2). Map hashCode() Method in Java with Examples. GeeksforGeeks. https://www.geeksforgeeks.org/map-hashcode-method-in-java-with-examples/?ref=lbp
 * 
 * barykrg. (2023, February 6). Math pow() method in Java with Example. GeeksforGeeks. https://www.geeksforgeeks.org/math-pow-method-in-java-with-example/
 * 
 * barykrg. (2024, February 16). Map put() Method in Java with Examples. GeeksforGeeks. https://www.geeksforgeeks.org/map-put-method-in-java-with-examples/?ref=lbp 
 * 
 * chinmoy lenka. (2023, January 11). HashMap get() Method in Java. GeeksforGeeks. https://www.geeksforgeeks.org/hashmap-get-method-in-java/?ref=lbp 
 * 
 * GeeksforGeeks. (2024, July 5). HashMap in Java. GeeksforGeeks. https://www.geeksforgeeks.org/java-util-hashmap-in-java-with-examples/?ref=lbp 
 * 
 * gopaldave. (2018, December 31). Map containsKey() method in Java with Examples. GeeksforGeeks. https://www.geeksforgeeks.org/map-containskey-method-in-java-with-examples/?ref=lbp 
 * 
 * kadambalamatclo. (2024, February 29). How to Implement a Custom Hash function for Keys in a HashMap in Java? GeeksforGeeks. https://www.geeksforgeeks.org/implement-a-custom-hash-function-for-keys-in-a-hashmap-in-java/
 * 
 * Thakkar, N. (2024, April 11). Global Variable in Java - Scaler topics. Scaler Topics. https://www.scaler.com/topics/global-variable-in-java/
 * 
 * Vu, N. T. (2024, June 6). Get the ASCII Value of a Character in Java | Baeldung. Baeldung. https://www.baeldung.com/java-character-ascii-value
 * 
 */




import java.util.ArrayList;
import java.util.Scanner;
import java.util.HashMap;
import java.lang.Math;

// Importing error checking.
import java.util.InputMismatchException;

// (Thakkar, 2024, Create Global Variables by Using Interfaces in Java section)
interface Values {
	int STARTEXPONENT = 0;
	double EXPONENTIALINCREASS = 0.07;
}

public class Driver {

	//Declaring and creating new list for both animals.
    private static ArrayList<Dog> dogList = new ArrayList<Dog>();
    private static ArrayList<Monkey> monkeyList = new ArrayList<Monkey>();

	// (GeeksforGeeks, 2024; barykrg, 2019), decaring and creating hashmaps for both dog and monkey
	private static HashMap<String, Dog> dogHashMap = new HashMap<String, Dog>();
	private static HashMap<String, Monkey> monkeyHashMap = new HashMap<String, Monkey>();

	// Declaring static variabels to get rid of magic numbers.
	static int QUIT = -1;
	static int NOERROR = -1;
	static int DOGPRINT = 4;
	static int MONKEYPRINT = 5;
	static int PRINTNOTRESERVED = 6;
	static int WAITPRINTLIST = 0;
	static int RUNPROGRAM = 1;

    public static void main(String[] args) {

		// Declaring variables for later use.
    	String userInput;
    	int printList = WAITPRINTLIST;
    	int dontQuit = RUNPROGRAM;
    	Scanner scnr = new Scanner(System.in);

		// Initializing animal lists.
        initializeDogList();
        initializeMonkeyList();
        
        // Displays the menu until q is entered.
        while (dontQuit != QUIT) {
        	displayMenu();
        	userInput = scnr.nextLine();
        	switch (userInput) {
        	
        	    // When q is input, the loop will stop.
        	    case "q":
        		    dontQuit = QUIT; // Stops the loop.
        		    break;
        		
        		// Takes user to the method to input new dog into list.
        	    case "1":
        		    intakeNewDog(scnr);
        		    break;
        	
        		// Takes user to method to input new monkey.
        	    case "2":
        		    intakeNewMonkey(scnr);
        		    break;
        		
        		// Takes user to the method to reserve an animal.
        	    case "3":
        		    reserveAnimal(scnr);
        		    break;
        	
        		// Prints out the dogs in the dog list.
        	    case "4":
        	    	printList = DOGPRINT;
        		    printAnimals(printList, scnr);
        		    break;
        		
        		// Prints out the monkeys in the monkey list.
        	    case "5":
        	    	printList = MONKEYPRINT;
        		    printAnimals(printList, scnr);
        		    break;
        	
        		// Prints out the available animals.
        	    case "6":
        	    	printList = PRINTNOTRESERVED;
        		    printAnimals(printList, scnr);
        		    break;

				// Added a search function to show off the hashmap functionality
				case "7":
					searchForAnimal(scnr);
					break;
        	
        		// If none of the other cases work, then user input is incorrect and the user is told such.
        	    default:
        			System.out.print("Incorrect input. Please try Again.\n");
        			break;
        	}

			// Lets the user read the warning or other text that pops up.
			if (!userInput.equals("q")) {
				waitForUserRead(scnr);
			}
        }
        

    }

    public static void displayMenu() {
        System.out.println("\n\n");
        System.out.println("\t\t\t\tRescue Animal System Menu");
        System.out.println("[1] Enter a new dog");
        System.out.println("[2] Enter a new monkey");
        System.out.println("[3] Reserve an animal");
        System.out.println("[4] Print a list of all dogs");
        System.out.println("[5] Print a list of all monkeys");
        System.out.println("[6] Print a list of all animals that are not reserved");
		System.out.println("[7] Search for a specific animal");
        System.out.println("[q] Quit application");
        System.out.println();
        System.out.print("Enter a menu selection: ");
    }


    public static void initializeDogList() {

		// Adding two dogs to the list to check for error
        Dog dog1 = new Dog("Spot", "German Shepherd", "male", 1, "25.6", "05-12-2019", "United States", "intake", false, "United States");
        Dog dog2 = new Dog("Rex", "Great Dane", "male", 3, "35.2", "02-03-2020", "United States", "Phase I", false, "United States");
        Dog dog3 = new Dog("Bella", "Chihuahua", "female", 4, "25.6", "12-12-2019", "Canada", "In Service", true, "Canada");
        
       // Added to test if option 6 worked.
        Dog dog4 = new Dog("Hello", "Sheltie", "female", 5, "22.4", "1-22-17", "United States", "In Service", false, "United States");
        dogList.add(dog1);
        dogList.add(dog2);
        dogList.add(dog3);
        dogList.add(dog4);


		// (GeeksforGeeks, 2024), Try to make unique keys to input into the hashmap, try to keep information simple so that users can search for the animal later.
		String dogKey1 = "Spot" +"German Shepherd" + "male" + "1" + "05-12-2019" + "United States";
		String dogKey2 = "Rex" + "Great Dane" +  "male" +  "3" + "02-03-2020" + "United States";
		String dogKey3 = "Bella" + "Chihuahua" + "female" + "4" + "12-12-2019" + "Canada";
		String dogKey4 = "Hello" + "Sheltie" + "female" + "5" + "1-22-17" + "United States";
		dogKey1 = dogKey1.replaceAll(" ", "").toLowerCase();
		dogKey2 = dogKey2.replaceAll(" ", "").toLowerCase();
		dogKey3 = dogKey3.replaceAll(" ", "").toLowerCase();
		dogKey4 = dogKey4.replaceAll(" ", "").toLowerCase();

		newKeyFunction dogKey1Complete = new newKeyFunction(dogKey1);
		newKeyFunction dogKey2Complete = new newKeyFunction(dogKey2);
		newKeyFunction dogKey3Complete = new newKeyFunction(dogKey3);
		newKeyFunction dogKey4Complete = new newKeyFunction(dogKey4);


		// (barykrg, 2024) Information entered into hashmap.
		dogHashMap.put(dogKey1Complete.getNewKey(), dog1);
		dogHashMap.put(dogKey2Complete.getNewKey(), dog2);
		dogHashMap.put(dogKey3Complete.getNewKey(), dog3);
		dogHashMap.put(dogKey4Complete.getNewKey(), dog4);
    }

    public static void initializeMonkeyList() {

    	// Adding two monkeys to the list to check for errors.
    	Monkey monkey1 = new Monkey("Test", "male", 12, "22.8", "1-22-17", "Test", false, "Test", "In Service", "United States", "Test", "Test", "Capuchin");
    	Monkey monkey2 = new Monkey("Testing", "female", 12, "22.8", "1-22-17", "Test", true, "Test", "In Service", "United States", "Test", "Test", "Test");
    	monkeyList.add(monkey1);
    	monkeyList.add(monkey2);

		// Try to make unique keys to input into the hashmap, try to keep information simple so that users can search for the animal later.
		String monkeyKey1 = "Test" + "Capuchin" + "male" + 12 + "1-22-17" + "Test";
		String monkeyKey2 = "Testing" + "TestSpecies" + "female" + 12 + "1-22-17" + "Test";
		monkeyKey1 = monkeyKey1.replaceAll(" ", "").toLowerCase();
		monkeyKey2 = monkeyKey2.replaceAll(" ", "").toLowerCase();

		newKeyFunction monkeyKey1Complete = new newKeyFunction(monkeyKey1);
		newKeyFunction monkeyKey2Complete = new newKeyFunction(monkeyKey2);

		// Information entered into hashmap
		monkeyHashMap.put(monkeyKey1Complete.getNewKey(), monkey1);
		monkeyHashMap.put(monkeyKey2Complete.getNewKey(), monkey2);
    }

    public static void intakeNewDog(Scanner scanner) {

    	// Declaring the variables for the new dog object.
    	String dogBreed;
    	String dogGender;
    	int dogAge;
    	String dogWeight;
    	String dogAcquisitionDate;
        String dogAcquisitionCountry;
        boolean dogReserved = false;
	    String dogInServiceCountry;
	    String dogTrainingStatus;
		String dogName;
		String userDogKey;

    	// Grabs the the info needed about the dog from the user.
        System.out.println("What is the dog's name?");
        dogName = scanner.nextLine();
        System.out.println("What is the dog's breed?");
        dogBreed = scanner.nextLine();
    	System.out.println("What is the dog's gender?");
    	dogGender = scanner.nextLine();

		// Checks if the dog's input age is an integer, returns if not after printing a warning message.
		try {
    		System.out.println("What is the dog's age? Please enter a whole number.");
    		dogAge = scanner.nextInt();
			scanner.nextLine();
		}
		catch (InputMismatchException e) {
			System.out.println("Error: Please enter a whole number.\n");
			scanner.nextLine();
			return;
		}

		// Continues gathering dog information.
    	System.out.println("What is the dog's weight?");
    	dogWeight = scanner.nextLine();
    	System.out.println("What is the dog's acquisition date?");
    	dogAcquisitionDate = scanner.nextLine();
    	System.out.println("What is the dog's acquisition location?");
    	dogAcquisitionCountry = scanner.nextLine();
		
		// (GeeksforGeeks, 2024), Creates the key for hashmap, checks if the dog is in the system.
		userDogKey = dogName + dogBreed + dogGender + dogAge + dogAcquisitionDate + dogAcquisitionCountry;
		userDogKey = userDogKey.replaceAll(" ", "").toLowerCase();

		newKeyFunction userDogKeyComplete = new newKeyFunction(userDogKey);

		if (dogHashMap.containsKey(userDogKeyComplete.getNewKey()) == true) { // (gopaldave, 2018), for the containskey function
			System.out.println("This dog is already in our system.");
			return;
		}
    	
    	// Checks if the dog's input reserved value is a boolean, returns if not after printing message.
    	try {
        	System.out.println("Is the dog reserved? (true/false)");
        	dogReserved = scanner.nextBoolean();
        }
        catch (InputMismatchException e) {
        System.out.println("Error: Please enter true or false.\n");
		scanner.nextLine();
		return;
        }
    	
    	scanner.nextLine(); // For next input.
    	
    	// Gets the rest of the information of the dog.
    	System.out.println("What is the dog's in service country?");
    	dogInServiceCountry = scanner.nextLine();
    	System.out.println("What is the dog's training status?");
        dogTrainingStatus = scanner.nextLine();

        // Checks for empty variables and outputs a message to the user before returning them to main menu.
		if (dogWeight.equals("") || dogAcquisitionCountry.equals("") || dogTrainingStatus.equals("") || dogAcquisitionDate.equals("") || 
		dogBreed.equals("") || dogGender.equals("") || dogInServiceCountry.equals("") || dogName.equals("") || dogTrainingStatus.equals("")) {
			System.out.println("One of the inputs is empty, please try again with correct input.");
			return;
		}

        // Creates a new dog object and adds that to the dog list and hashmap.
        Dog dog = new Dog(dogName, dogBreed, dogGender, dogAge, dogWeight, dogAcquisitionDate, dogAcquisitionCountry, dogTrainingStatus, dogReserved, dogInServiceCountry);
        dogList.add(dog);

		dogHashMap.put(userDogKeyComplete.getNewKey(), dog); // (barykrg, 2024)
    }

        public static void intakeNewMonkey(Scanner scanner) {

        	// Declaring all the variables that will be needed to create a new monkey object that will be added to the list/hashmap.
        	String monkeyName;
        	String monkeyGender;
        	int monkeyAge;
        	String monkeyWeight;
        	String monkeyAcquisitionDate;
            String monkeyAcquisitionCountry;
            boolean monkeyReserved = false;
 	        String monkeyInServiceCountry;
 	        String monkeyTrainingStatus;
 	        String monkeyTailLength;
 	        String monkeyHeight;
 	        String monkeyBodyLength;
 	        String monkeySpecies;
			String userMonkeyKey;
        	
        	// Checks if the monkey's species is a valid species.
        	System.out.println("What is the monkey's species?");
        	monkeySpecies = scanner.nextLine();
        	if (monkeySpecies.equalsIgnoreCase("Capuchin") || monkeySpecies.equalsIgnoreCase("Guenon") || monkeySpecies.equalsIgnoreCase("Macaque") || 
            monkeySpecies.equalsIgnoreCase("Marmoset") || monkeySpecies.equalsIgnoreCase("Squirrel monkey") || monkeySpecies.equalsIgnoreCase("Tamarin")) {
        		
        		// The rest of the information that is needed about the monkey is input from the user with their respective prompts.
				System.out.println("What is the monkey's name?");
				monkeyName = scanner.nextLine();
            	System.out.println("What is the monkey's gender?");
            	monkeyGender = scanner.nextLine();

            	// Checks if the monkey's input age is an integer, returns if not after printing a warning message.
				try {
					System.out.println("What is the monkey's age? Please enter a whole number.");
					monkeyAge = scanner.nextInt();
					scanner.nextLine();
				}
				catch (InputMismatchException e) {
					System.out.println("Error: Please enter a whole number.\n");
					scanner.nextLine();
					return;
				};

				// Continues gathering monkey information
            	System.out.println("What is the monkey's weight?");
            	monkeyWeight = scanner.nextLine();
            	System.out.println("What is the monkey's acquisition date?");
            	monkeyAcquisitionDate = scanner.nextLine();
            	System.out.println("What is the monkey's acquisition location?");
            	monkeyAcquisitionCountry = scanner.nextLine();

				// (GeeksforGeeks, 2024), Creates the key for hashmap, checks if the monkey is in the system.
				userMonkeyKey = monkeyName + monkeySpecies + monkeyGender + monkeyAge + monkeyAcquisitionDate + monkeyAcquisitionCountry;
				userMonkeyKey = userMonkeyKey.replaceAll(" ", "").toLowerCase();
				newKeyFunction userMonkeyKeyComplete = new newKeyFunction(userMonkeyKey);
				if (monkeyHashMap.containsKey(userMonkeyKeyComplete.getNewKey()) == true) { // (gopaldave, 2018), for the containskey function
					System.out.println("This monkey is already in ours system.");
					return;
				}
            	
            	// Checks if the monkey's input reserved value is a boolean, returns if not after printing message.
            	try {
                	System.out.println("Is the monkey reserved? (true/false)");
                	monkeyReserved = scanner.nextBoolean();
                }
                catch (InputMismatchException e) {
                    System.out.println("Error: Please enter true or false.\n");
                	scanner.nextLine();
                };

        	    scanner.nextLine(); // Gets to the next line for next input.
        	    
            	// Gets the rest of the info after the reserve information.
            	System.out.println("What is the monkey's in service country?");
            	monkeyInServiceCountry = scanner.nextLine();
            	System.out.println("What is the monkey's training status?");
                monkeyTrainingStatus = scanner.nextLine();
                System.out.println("What is the monkey's tail length?");
            	monkeyTailLength = scanner.nextLine();
            	System.out.println("What is the monkey's height?");
            	monkeyHeight = scanner.nextLine();
            	System.out.println("What is the monkey's body length?");
            	monkeyBodyLength = scanner.nextLine();
            	
				// Checks for empty variables and outputs a message to the user before returning them to main menu.
				if (monkeyWeight.equals("") || monkeyAcquisitionCountry.equals("") || monkeyTrainingStatus.equals("") || monkeyAcquisitionDate.equals("") || 
				monkeySpecies.equals("") || monkeyGender.equals("") || monkeyInServiceCountry.equals("") || monkeyName.equals("") || monkeyTrainingStatus.equals("") || 
				monkeyBodyLength.equals("") || monkeyTailLength.equals("") || monkeyHeight.equals("")) {
					System.out.println("One of the inputs is empty, please try again with correct input.");
					return;
				}

            	// Creates new monkey object and adds it to the list and hashmap with the information.
            	Monkey monkey = new Monkey(monkeyName, monkeyGender, monkeyAge, monkeyWeight, monkeyAcquisitionDate, monkeyAcquisitionCountry, monkeyReserved, monkeyInServiceCountry, monkeyTrainingStatus,
            	monkeyTailLength, monkeyHeight, monkeyBodyLength, monkeySpecies);
            	monkeyList.add(monkey);

				monkeyHashMap.put(userMonkeyKeyComplete.getNewKey(), monkey); // (barykrg, 2024)
        	}
        	
        	// If the species can not be entered, the program will output that to the user and return to the menu.
        	else {
        		System.out.println("That species of monkey can not be entered.");
        		return;
        	}
            
        }

        public static void reserveAnimal(Scanner scanner) {
        	// Declares variables that will be used later.
        	String animalType;
        	String animalInServiceCountry;
        	
        	// Asks the user what animal type they want and stores the information.
        	System.out.println("Do you want a monkey or a dog?");
        	animalType = scanner.nextLine();
        	
        	// Checks if user wants a dog.
        	if (animalType.equalsIgnoreCase("Dog")) {
        		
        		// Checks if there is a dog in the country available.
        		System.out.println("What is the dog's in service country");
            	animalInServiceCountry = scanner.nextLine();
            	
            	// Checks if there is a dog in the list that can be reserved.
            	for (Dog dog: dogList) {
            		if (dog.getInServiceLocation().equalsIgnoreCase(animalInServiceCountry) && dog.getTrainingStatus().equalsIgnoreCase("In Service") && 
            		dog.getReserved() == false) {
            		
            			dog.setReserved(true); 
            			System.out.println("Dog has been reserved.");
            			return; // Stops the for loop so multiple dogs can not be reserved.
            		}
            	}
            	
            	// Tells the user that there is not a dog that can be reserved.
    			System.out.println("There is not a dog that can be reserved in this location.");
        	}
        	
        	// Checks if the user wants a monkey.
        	else if (animalType.equalsIgnoreCase("Monkey")) {
        		
        		// Asks and grabs the user's information about the monkey's service country.
        		System.out.println("What is the monkey's in service country?");
            	animalInServiceCountry = scanner.nextLine();
            	
            	// Checks if a monkey in the list fits the user's wants and reserves the monkey.
            	for (Monkey monkey: monkeyList) {
            		if (monkey.getInServiceLocation().equalsIgnoreCase(animalInServiceCountry) && monkey.getTrainingStatus().equalsIgnoreCase("In Service") && 
            		monkey.getReserved() == false) {
            			monkey.setReserved(true);
            			System.out.println("Monkey has been reserved."); // Tells user that a monkey has been reserved.
            			return; // Stops at first monkey in the list that can be reserved at this location.
            		}
            	}
            	
            	// Prints out that there is not a monkey that can be reserved to the user.
    			System.out.println("There is not a monkey that can be reserved in this location.");
        	}
        	
        	// Tells the user that that animal type is not here.
        	else {
        		System.out.println("We do not have that animal type here.");
        	}
        	
        }
       
        // I added the integer printList here to figure out which list needed to be printed. 
        public static void printAnimals(int printList, Scanner scanner) {

        	// Switch statement to print out the right list.
        	switch (printList) {
        	
        	    // Prints out the dogs in the list.
        	    case 4:
					System.out.println("DOGS:");
        	    	for (Dog dog: dogList) {
						System.out.println(dog.getName() + ", " + dog.getTrainingStatus() + ", " + dog.getAcquisitionLocation() + ", " + dog.getReserved());
					}
        	    	break;
        	    
        	    // Prints out the monkeys in the list.
        	    case 5:
        	    	System.out.println("MONKEYS:");
        	    	for (Monkey monkey: monkeyList) {
						System.out.println(monkey.getName() + ", " + monkey.getTrainingStatus() + ", " + monkey.getAcquisitionLocation() + ", " + monkey.getReserved());
					}
        	    	break;
        	    	
        	    // Prints out the dogs and the monkeys that are available and are trained to the user.
        	    case 6:
        	    	System.out.println("DOGS:"); // Prints out DOGS to make this more readable.
        	    	
        	    	// Checks if the dogs is trained and if it is not reserved for every dog in the list and prints out the dog if it is.
        	    	for (Dog dog: dogList) {
        	    		if((dog.getTrainingStatus().equalsIgnoreCase("In Service") == true) && (dog.getReserved() == false)) {
        	    			System.out.println(dog.getName() + ", " + dog.getTrainingStatus() + ", " + dog.getAcquisitionLocation() + ", " + "Not Reserved.");
        	    		}
        	    	}
        	    	System.out.println("\n"); // Prints out newline to make it more readable.
        	    	
        	    	System.out.println("MONKEYS:"); // Prints out MONKEYS to split apart the lists.
        	    	
        	    	// Checks if each monkey in the list is trained and is not reserved, and when a monkey is both, it is printed out to the user.
        	    	for (Monkey monkey: monkeyList) {
        	    		if (monkey.getTrainingStatus().equalsIgnoreCase("In Service") && monkey.getReserved() == false) {
        	    			System.out.println(monkey.getName() + ", " + monkey.getTrainingStatus() + ", " + monkey.getAcquisitionLocation() + ", " + "Not Reserved.");
        	    		}
        	    	}
        	    	break;
        	}
        }

		// Function waits for the user to see the list instead of printing the main menu immediatly after printing the lists.
		public static void waitForUserRead(Scanner scanner) {
			String continueToMainMenu;
			int loopWaitList = WAITPRINTLIST;

			System.out.print("\nContinue? (yes/no) ");

			// While loop to wait for user input yes.
			while (loopWaitList != QUIT) {
				continueToMainMenu = scanner.nextLine();
				switch (continueToMainMenu) {
					case "yes":
					loopWaitList = QUIT;
						break;
			
					default:
					System.out.print("Please enter yes to continue back to the main menu: ");
						break;
				}
			}
		}

		public static void searchForAnimal(Scanner scanner) {
			
			// Variables used for search.
			String userInput;
			String animalKeySearch = "";
			Dog dog;
			Monkey monkey;

			System.out.print("Do you want to search for a monkey or a dog?: ");
			userInput = scanner.nextLine();
	
			if (userInput.equalsIgnoreCase("dog") == true) {
				
				// Grabs the the info needed about the dog from the user.
				System.out.println("What is the dog's name?");
				animalKeySearch += scanner.nextLine();
				System.out.println("What is the dog's breed?");
				animalKeySearch += scanner.nextLine();
				System.out.println("What is the dog's gender?");
				animalKeySearch += scanner.nextLine();
				
				// Checks if the dog's input age is an integer, returns if not after printing a warning message.
				try {
					System.out.println("What is the dog's age? Please enter a whole number.");
					animalKeySearch += scanner.nextInt();
				}
				catch (InputMismatchException e) {
					System.out.println("Error: Please enter a whole number.\n");
					return;
				}
				
				// Continues gathering dog information.
				animalKeySearch += scanner.nextLine();
				System.out.println("What is the dog's acquisition date?");
				animalKeySearch += scanner.nextLine();
				System.out.println("What is the dog's acquisition location?");
				animalKeySearch += scanner.nextLine();

				animalKeySearch = animalKeySearch.replaceAll(" ", "").toLowerCase();
				newKeyFunction animalKeySearchComplete = new newKeyFunction(animalKeySearch);
				if (dogHashMap.containsKey(animalKeySearchComplete.getNewKey()) == true) { // (gopaldave, 2018), for the containskey function
					dog = dogHashMap.get(animalKeySearchComplete.getNewKey()); // (chinmoy lenka, 2023), get funciton.
					System.out.println("Dog information: " + dog.getName() + ", " + dog.getGender() + ", " + dog.getDogBreed() + ", " + dog.getAge() + ", " + dog.getWeight() + 
					", " + dog.getTrainingStatus() + ", " + dog.getAcquisitionDate() + ", Aquisition Location: " + dog.getAcquisitionLocation() + ", Service Location: " + 
					dog.getInServiceLocation() + ", " + dog.getReserved());
					return;
				}
				else {
					System.out.println("This dog is not in our system.");
				}

			}
			else if (userInput.equalsIgnoreCase("monkey")) {

				// The rest of the information that is needed about the monkey is input from the user with their respective prompts.
				System.out.println("What is the monkey's name?");
				animalKeySearch += scanner.nextLine();
				System.out.println("What is the monkey's species?");
				animalKeySearch += scanner.nextLine();
				System.out.println("What is the monkey's gender?");
				animalKeySearch += scanner.nextLine();

				// Checks if the monkey's input age is an integer, returns if not after printing a warning message.
				try {
					System.out.println("What is the monkey's age? Please enter a whole number.");
					animalKeySearch += scanner.nextInt();
					scanner.nextLine();
				}
				catch (InputMismatchException e) {
					System.out.println("Error: Please enter a whole number.\n");
					return;
				};

				// Continues gathering monkey information
				System.out.println("What is the monkey's acquisition date?");
				animalKeySearch += scanner.nextLine();
				System.out.println("What is the monkey's acquisition location?");
				animalKeySearch += scanner.nextLine();

				animalKeySearch = animalKeySearch.replaceAll(" ", "").toLowerCase();
				newKeyFunction animalKeySearchComplete = new newKeyFunction(animalKeySearch);
				if (monkeyHashMap.containsKey(animalKeySearchComplete.getNewKey()) == true) { // (gopaldave, 2018), for the containskey function
					monkey = monkeyHashMap.get(animalKeySearchComplete.getNewKey()); // (chinmoy lenka, 2023), get funciton.
					System.out.println("Monkey information: " + monkey.getName() + ", " + monkey.getMonkeySpecies() + ", " + monkey.getGender() + ", " + monkey.getMonkeyBodyLength() + 
					", " + monkey.getMonkeyTailLength() + ", " + monkey.getMonkeyHeight() + ", " + monkey.getAge() + ", " + monkey.getWeight() + ", " + 
					monkey.getTrainingStatus() + ", " + monkey.getAcquisitionDate() + ", Aquisition Location: " + monkey.getAcquisitionLocation() + ", Service Location: " + 
					monkey.getInServiceLocation() + ", " + monkey.getReserved());
					return;
				}
				else {
					System.out.println("This monkey is not in our system.");
				}
			}

			else {
				System.out.println("That animal is not in our system, please try again");
				return;
			}

		}
}


// (kadambalamatclo, 2024)
class newKeyFunction {

	// Declaring variables for the hash function.
	int newKeyCreation;
	char functionChangeKey[];
	double newKeyHashCodeCalculate = 0;
	int newKeyHashCode = 0;
	double exponential = Values.STARTEXPONENT;
	boolean changeCharValue = true;
	private String newKey;

	// Sets the key to the string from user input
	public newKeyFunction (String newDataKey) {
		this.newKey = newDataKey;
	}

	// Returns the key as a string.
	public String getNewKey() {
		return this.newKey;
	}

	// Hashfunction for the hashcode
	@Override
	public int hashCode() {

		functionChangeKey = getNewKey().toCharArray();

		// Calculates hash funciton
		for (char characterInKey : functionChangeKey) {

			// (Vu, 2024; barykrg, 2023), Calculates and adds to the hashcode.
			newKeyHashCodeCalculate += (characterInKey * (Math.pow(10, exponential)));
			exponential = exponential + Values.EXPONENTIALINCREASS;
		}

		// Makes the value an int at the very end so not much data is lost.
		newKeyHashCode = (int)newKeyHashCodeCalculate;

		// Returns the hashcode for the hashmap.
		return newKeyHashCode;
	}
}
```

### RescueAnimal.java
```java


import java.lang.String;

public class RescueAnimal {

    // Instance variables
    private String name;
    private String animalType;
    private String gender;
    private int age;
    private String weight;
    private String acquisitionDate;
    private String acquisitionCountry;
	private String trainingStatus;
    private boolean reserved;
	private String inServiceCountry;


    // Constructor
    public RescueAnimal() {
    }

	// Setters & Getters
	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}


	public String getAnimalType() {
		return animalType;
	}


	public void setAnimalType(String animalType) {
		this.animalType = animalType;
	}


	public String getGender() {
		return gender;
	}


	public void setGender(String gender) {
		this.gender = gender;
	}


	public int getAge() {
		return age;
	}


	public void setAge(int age) {
		this.age = age;
	}


	public String getWeight() {
		return weight;
	}


	public void setWeight(String weight) {
		this.weight = weight;
	}


	public String getAcquisitionDate() {
		return acquisitionDate;
	}


	public void setAcquisitionDate(String acquisitionDate) {
		this.acquisitionDate = acquisitionDate;
	}


	public String getAcquisitionLocation() {
		return acquisitionCountry;
	}


	public void setAcquisitionLocation(String acquisitionCountry) {
		this.acquisitionCountry = acquisitionCountry;
	}


	public boolean getReserved() {
		return reserved;
	}


	public void setReserved(boolean reserved) {
		this.reserved = reserved;
	}


	public String getInServiceLocation() {
		return inServiceCountry;
	}


	public void setInServiceCountry(String inServiceCountry) {
		this.inServiceCountry = inServiceCountry;
	}


	public String getTrainingStatus() {
		return trainingStatus;
	}


	public void setTrainingStatus(String trainingStatus) {
		this.trainingStatus = trainingStatus;
	}
}
```

### Dog.java
```java

public class Dog extends RescueAnimal {

    // Instance variable
    private String breed;

    // Constructor
    public Dog(String name, String breed, String gender, int age,
    String weight, String acquisitionDate, String acquisitionCountry,
	String trainingStatus, boolean reserved, String inServiceCountry) {
        setName(name);
        setDogBreed(breed);
        setGender(gender);
        setAge(age);
        setWeight(weight);
        setAcquisitionDate(acquisitionDate);
        setAcquisitionLocation(acquisitionCountry);
        setTrainingStatus(trainingStatus);
        setReserved(reserved);
        setInServiceCountry(inServiceCountry);

    }

    // Accessor Method
    public String getDogBreed() {
        return breed;
    }

    // Mutator Method
    public void setDogBreed(String dogBreed) {
        breed = dogBreed;
    }

}
```

### Monkey.java
```java

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
```
