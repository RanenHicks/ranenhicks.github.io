<!-- (Adding content to your GitHub Pages site using Jekyll, n.d.) -->

# Algorithms and Data Structures

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

