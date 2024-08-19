from ProjectTwoRanenHicks import AnimalShelter
import sqlite3

# Global variables for magic numbers
ASCIIVAL = 48
ID = 0
AGEUPON = 1
ANIMALID = 2
ANIMALTYPE = 3
BREED = 4
COLOR = 5
DATEOFBIRTH = 6
DATETIME = 7
MONTHYEAR = 8
NAME = 9
OUTCOMESUBTYPE = 10
OUTCOMETYPE = 11
SEXUPONOUTCOME = 12
LOCATIONLAT = 13
LOCATIONLONG = 14
AGEUPONWEEKS = 15
MAXLIST = 14

# Connects to the two databases
dataBase = AnimalShelter("accUser", "accPass")
dataBaseSql = sqlite3.connect("db.sqlite3") # (Sqlite3 — DB-API 2.0 Interface for SQLite Databases, 2024)

# Updates the SQLite3 database
def updateSQL():

    # Deletes the data stored in the database to stop collisions
    dataBaseSql.execute("DELETE FROM database_animalmodel") # (Sqlite3 — DB-API 2.0 Interface for SQLite Databases, 2024)

    # Gets data from the MongoDB database
    resultMongo = dataBase.read({})
    dictionaryToTuple = [] #list for later
    
    # Seperates each entry from the whole database
    for dictionary in resultMongo:

        # List to store edited MongoDB information
        string = [] 

        # (Sanchithasr, 2022) Splits each entry into the data fields.
        stringDictionary = str(dictionary).split(',')

        # (striver, 2024), Edits the data to remove dictionary parts to leave a clean list. Does this for each data field. 
        # Also 1 is added since ID is the second field from MongoDB.
        string.append(stringDictionary[ID + 1].replace("'id': ", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[AGEUPON + 1].replace("'age_upon_outcome': ", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[ANIMALID + 1].replace("'animal_id': ", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[ANIMALTYPE+ 1].replace("'animal_type': ", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[BREED + 1].replace("'breed': ", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[COLOR + 1].replace("'color': ", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[DATEOFBIRTH + 1].replace("'date_of_birth': ", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[DATETIME + 1].replace("'datetime':", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[MONTHYEAR + 1].replace("'monthyear':", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[NAME + 1].replace("'name':", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[OUTCOMESUBTYPE + 1].replace("'outcome_subtype':", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[OUTCOMETYPE + 1].replace("'outcome_type':", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[SEXUPONOUTCOME + 1].replace("'sex_upon_outcome': ", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[LOCATIONLAT + 1].replace("'location_lat': ", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[LOCATIONLONG + 1].replace("'location_long': ", "").replace(" ", "").replace("'", ""))
        string.append(stringDictionary[AGEUPONWEEKS + 1].replace("'age_upon_outcome_in_weeks': ", "").replace(" ", "").replace("'", "").replace("}", ""))

        iterator = 0 #iterator for null entries
        
        # Checks for null entries
        for stringNullCheck in string:

            # Makes sure the iterator does not go out of list bounds
            if iterator == MAXLIST:
                iterator = 0

            # (Clark, 2022), Changes null entries to N/A
            if stringNullCheck == "":
                stringNullCheck = "N/A"
                string[iterator] = stringNullCheck
            iterator += 1

        # (GeeksforGeeks, 2023), Changes the data type to a tuple to insert into SQLite3
        dictionaryToTuple = tuple(string)

        # (Sqlite3 — DB-API 2.0 Interface for SQLite Databases, 2024), Inserts the tuple into the SQLite3 database.
        addToDatabase = "INSERT INTO database_animalmodel VALUES " + str(dictionaryToTuple)
        dataBaseSql.execute(addToDatabase)
    dataBaseSql.commit() # (unutbu, 2017)


# Updates the MongoDB database with data from SQLite3 database
def updateMongoDB():

    # (Sqlite3 — DB-API 2.0 Interface for SQLite Databases, 2024) Gets data from SQLite3 database.
    result = dataBaseSql.execute("SELECT * FROM database_animalmodel")

    # Deletes data from MongoDB database to stop duplicate objects.
    dataBase.delete({})

    dictionaryDataConvert = [] # To store data later

    # Edits data from SQLite3 to put into MongoDB
    for data in result:

        # (anushka_jain_gfg, 2023), Converts the tuple into a list and puts it into another list to edit later
        dictionaryDataConvert.append(list(data))

    # Grabs each object and converts it into a dictionary type
    for convertData in dictionaryDataConvert:

        # (pulamolusaimohan, 2024)
        dictionaryData = dict(id = convertData[ID], age_upon_outcome = convertData[AGEUPON], animal_id = convertData[ANIMALID], animal_type = convertData[ANIMALTYPE], 
                        breed = convertData[BREED], color = convertData[COLOR], date_of_birth = convertData[DATEOFBIRTH], datetime = convertData[DATETIME], 
                        monthyear = convertData[MONTHYEAR], name = convertData[NAME], outcome_subtype = convertData[OUTCOMESUBTYPE], outcome_type = convertData[OUTCOMETYPE],
                        sex_upon_outcome = convertData[SEXUPONOUTCOME], location_lat = convertData[LOCATIONLAT], location_long = convertData[LOCATIONLONG],
                        age_upon_outcome_in_weeks = convertData[AGEUPONWEEKS])
        
        # Submits data to MongoDB database
        dataBase.create(dictionaryData)

# User interface to update the databases
def inputUpdate():
    userInput = input("Do you want to update \nSQL (1): If any changes were made to MongoDB \nMongoDB (2): If any changes were made to SQL.\nInput: ")
    if userInput == "1":
        updateSQL()
    elif userInput == "2":
        updateMongoDB()
    else:
        print("Incorrect input, please try again")

# Calls the interface when the file is run
inputUpdate()
