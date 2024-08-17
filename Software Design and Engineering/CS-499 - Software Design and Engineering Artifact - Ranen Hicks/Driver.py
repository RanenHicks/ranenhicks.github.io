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
from ContactService import ContactService
from TaskService import TaskService
import datetime

CONTINUERUNNING = True

# Initializes lists
appointmentList = []
contactList = []
taskList = []


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
    print("\nContact Service\n")
    print("What would you like to do?:")
    print("[1] Add Contact")
    print("[2] Delete Contact")
    print("[3] Update Contact")
    print("[4] Main Menu")


def printTaskServiceMenu():
    print("\nTask Service\n")
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
    userAppointment = appointmentServices.AppointmentService(True, False, appointmentList, userAppointmentid, userAppointmentDate, userAppointmentDescription)
    
    # Checking for correct addition and adding to list if so
    if appointmentServices.added == True:
        print("Appointment added correctly")
        appointmentList.append(userAppointment)
        return


def askDeleteAppointmentService():
    
    # Only id is needed since it is unique
    userAppointmentid = input("Please enter an appointment id (10 or less characters): ")

    # Deletes the contact
    appointmentServices.AppointmentService(False, True, appointmentList, userAppointmentid, None, None)
    if appointmentServices.deleted == True:
        print("Appointment Deletion Complete")

# Contact service functions
def askAddContactService():

    # Getting user contact information
    userContactid = input("Please enter a contact id (10 or less characters): ")
    userContactFirstName = input("Please enter contact first name: ")
    userContactLastName = input("Please enter contact last name ")
    userContactPhoneNumber = input("Please enter contact phone number (no '-'): ")
    userContactDescription = input("Please enter an contact address (30 or less characters): ")

    userContact = contactServices.ContactService(True, False, False, contactList, userContactid, userContactFirstName, userContactLastName, userContactPhoneNumber, userContactDescription)
    
    # Checking for correct addition and adding to list if so
    if contactServices.added == True:
        print("Contact added correctly")
        contactList.append(userContact)
        return


def askDeleteContactService():
    
    # Only id is needed since it is unique
    userContactid = input("Please enter an contact id (10 or less characters): ")

    # Deletes the contact
    contactServices.ContactService(False, True, False, contactList, userContactid, None, None, None, None)
    if contactServices.deleted == True:
        print("Contact Deletion Complete")

def askUpdateContactService():
    
    # Getting user contact information
    userContactid = input("Please enter a contact id to update (10 or less characters): ")
    userContactFirstName = input("Please enter updated contact first name: ")
    userContactLastName = input("Please enter updated contact last name ")
    userContactPhoneNumber = input("Please enter updated contact phone number (no '-'): ")
    userContactAddress = input("Please enter updated contact address (30 or less characters): ")

    contactServices.ContactService(False, False, True, contactList, userContactid, userContactFirstName, userContactLastName, userContactPhoneNumber, userContactAddress)
    
    # Checking for correct addition and adding to list if so
    if contactServices.updated == True:
        print("Contact updated correctly")
        return
    
# Task service functions
def askAddTaskService():

    # Getting user task id input
    userTaskid = input("Please enter an task id (10 or less characters): ")

    # Checks for non-integer input
    try:
        userTaskYear = int(input("Please enter an task year: "))
        userTaskMonth = int(input("Please enter an task month: "))
        userTaskDay = int(input("Please enter an task day: "))
    except ValueError:
        print("Please enter an integer for the date values.")
        
        # Puts the user into the task menu
        return
    
    # Getting user task description input
    userTaskDescription = input("Please enter an task description (50 or less characters): ")

    # Sets date to the correct type and enters information
    userTaskDate = datetime.date(userTaskYear, userTaskMonth, userTaskDay)
    userTask = taskServices.TaskService(True, False, False, taskList, userTaskid, userTaskDate, userTaskDescription)
    
    # Checking for correct addition and adding to list if so
    if taskServices.added == True:
        print("Task added correctly")
        taskList.append(userTask)
        return


def askDeleteTaskService():
    
    # Only id is needed since it is unique
    userTaskid = input("Please enter an task id (10 or less characters): ")

    # Deletes the contact
    taskServices.TaskService(False, True, False, taskList, userTaskid, None, None)
    if taskServices.deleted == True:
        print("Task Deletion Complete")

    # Task service functions
def askUpdateTaskService():

    # Getting user task id input
    userTaskid = input("Please enter a task id to update (10 or less characters): ")

    # Checks for non-integer input
    try:
        userTaskYear = int(input("Please enter updated task year: "))
        userTaskMonth = int(input("Please enter updated task month: "))
        userTaskDay = int(input("Please enter updated task day: "))
    except ValueError:
        print("Please enter an integer for the date values.")
        
        # Puts the user into the task menu
        return
    
    # Getting user task description input
    userTaskDescription = input("Please enter an updated task description (50 or less characters): ")

    # Sets date to the correct type and enters information
    userTaskDate = datetime.date(userTaskYear, userTaskMonth, userTaskDay)
    userTask = taskServices.TaskService(False, False, True, taskList, userTaskid, userTaskDate, userTaskDescription)
    
    # Checking for correct addition and adding to list if so
    if taskServices.added == True:
        print("Task added correctly")
        taskList.append(userTask)
        return


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
            logicContactMenu()
        elif userInput == "3":
            logicTaskMenu()
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

def logicContactMenu():
    
    # Runs menu until user quits or goes to another menu
    runContactMenu = True
    while runContactMenu == CONTINUERUNNING:
        printContactServiceMenu()
        userInput = input()
        if userInput == "1":
            askAddContactService()
        elif userInput == "2":
            askDeleteContactService()
        elif userInput == "3":
            askUpdateContactService()
        elif userInput == "4":
            runContactMenu = False
        else:
            print("Invalid command")
    return

def logicTaskMenu():
    
    # Runs menu until user quits or goes to another menu
    runTaskMenu = True
    while runTaskMenu == CONTINUERUNNING:
        printTaskServiceMenu()
        userInput = input()
        if userInput == "1":
            askAddTaskService()
        elif userInput == "2":
            askDeleteTaskService()
        elif userInput == "3":
            askUpdateTaskService()
        elif userInput == "4":
            runTaskMenu = False
        else:
            print("Invalid command")
    return


# (Kalra, 2023; Everythingtech, 2023), initializes services
appointmentServices = AppointmentService(None, None, None, None, None, None)
contactServices = ContactService(None, None, None, None, None, None, None, None, None)
taskServices = TaskService(None, None, None, None, None, None, None)

programRunning = True

while programRunning == CONTINUERUNNING:
    programRunning = logicMainMenu()

# Quits Program
SystemExit