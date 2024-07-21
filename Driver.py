# Author: Ranen Hicks
# Date: 7/21/2024
# Summary: This program allows the user to add and delete appointments, contacts, and tasks using the command prompt. The contacts and tasks can also be updated using the
# command prompt. There are also unit tests that check the security of the program, in which each main file has a test file accompanying it.
#
# This code was created referencing python documentation: https://docs.python.org
#
# Other references:
# Erakshaya485. (2024, February 5). What is a clean and Pythonic way to have multiple constructors in Python? GeeksforGeeks.
#   https://www.geeksforgeeks.org/creating-multiple-constructors-python-class/
# Everythingtech. (2023, April 18). How to fix    typeerror  module  object is not callable  in Python. GeeksforGeeks.
#   https://www.geeksforgeeks.org/how-to-fix-typeerror-module-object-is-not-callable-in-python/
# Gyanendra371. (2024, July 5). self in Python class. GeeksforGeeks. https://www.geeksforgeeks.org/self-in-python-class/
# Kalra, S. (2023, March 27). Why do I get “TypeError: Missing 1 required positional argument: ‘self’”? (K. Knechtel & Wjandrea, Eds.). 
# Stack Overflow. https://stackoverflow.com/a/63738387
# Rollbar Editorial Team. (2023, July 23). How to throw exceptions in Python. Rollbar. https://rollbar.com/blog/throwing-exceptions-in-python/
# TerryA. (2013, September 25). Make python code continue after exception. Stack Overflow. https://stackoverflow.com/a/18994347


# (Everythingtech, 2023)
from AppointmentService import AppointmentService
import Appointment
import datetime

CONTINUERUNNING = True

# Initializes appointment list
appointmentList = []


# Print Menus
def printMainMenu():
    print("\nWelcome to the Appointment, Contact, and Task services program.\n")
    print("What task would you like to use?:")
    print("[1]: Appointment Service")
    print("[2]: Contact Service")
    print("[3]: Task Service")
    print("[4]: Quit")


def printAppointmentServiceMenu():
    print("\nAppointment Service\n")
    print("What would you like to do?:")
    print("[1] Add Appointment")
    print("[2] Delete Appointment")
    print("[3] Main Menu")


def printContactServiceMenu():
    print("Contact Service\n")
    print("What would you like to do?:")
    print("[1] Add Contact")
    print("[2] Delete Contact")
    print("[3] Update Contact")
    print("[4] Main Menu")


def printTaskServiceMenu():
    print("Task Service\n")
    print("What would you like to do?:")
    print("[1] Add Task")
    print("[2] Delete Task")
    print("[3] Update Task")
    print("[4] Main Menu")


# Appointment service functions
def askAddAppointmentService():

    # Getting user appointment id input
    userAppointmentid = input("Please enter an appointment id (10 or less characters): ")

    # Checks for non-integer input
    try:
        userAppointmentYear = int(input("Please enter an appointment year: "))
        userAppointmentMonth = int(input("Please enter an appointment month: "))
        userAppointmentDay = int(input("Please enter an appointment day: "))
    except ValueError:
        print("Please enter an integer for the date values.")
        
        # Puts the user into the appointment menu
        return
    
    # Getting user appointment description input
    userAppointmentDescription = input("Please enter an appointment description (50 or less characters): ")

    # Sets date to the correct type and enters information
    userAppointmentDate = datetime.date(userAppointmentYear, userAppointmentMonth, userAppointmentDay)
    userAppointment = AppointmentServices.AppointmentService(True, False, appointmentList, userAppointmentid, userAppointmentDate, userAppointmentDescription)
    
    # Checking for correct addition and adding to list if so
    if userAppointment.addedCorrectly == True:
        print("Appointment added correctly")
        appointmentList.append(userAppointment)
        return


def askDeleteAppointmentService():
    
    # Only id is needed since it is unique
    userAppointmentid = input("Please enter an appointment id (10 or less characters): ")

    # Deletes the appointment
    AppointmentServices.AppointmentService(False, True, appointmentList, userAppointmentid, None, None)
    if AppointmentServices.deleted == True:
        print("Appointment Deletion Complete")


# Logic for menus
def logicMainMenu():

    # Runs menu until user quits or goes to another menu
    runMainMenu = True
    while runMainMenu == CONTINUERUNNING:
        printMainMenu()
        userInput = input()
        if userInput == "1":
            logicAppointmentMenu()
        elif userInput == "2":
            printTaskServiceMenu()
        elif userInput == "3":
            printContactServiceMenu()
        elif userInput == "4":
            runMainMenu = False
        else:
            print("Invalid commands")
    return False


def logicAppointmentMenu():
    
    # Runs menu until user quits or goes to another menu
    runAppointmentMenu = True
    while runAppointmentMenu == CONTINUERUNNING:
        printAppointmentServiceMenu()
        userInput = input()
        if userInput == "1":
            askAddAppointmentService()
        elif userInput == "2":
            askDeleteAppointmentService()
        elif userInput == "3":
            runAppointmentMenu = False
        else:
            print("Invalid command")
    return


# Temporary main function to run program
# (Kalra, 2023; Everythingtech, 2023), initializes appointment service
AppointmentServices = AppointmentService(None, None, None, None, None, None)

programRunning = True

while programRunning == CONTINUERUNNING:
    programRunning = logicMainMenu()

# Quits Program
SystemExit