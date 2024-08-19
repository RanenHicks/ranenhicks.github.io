<!-- (Github basic writing and formatting syntax, n.d.; jonikarppinen, 2019; Mendelssohn, 2022; Adding content to your GitHub Pages site using Jekyll, n.d.) -->
[Go Back](README.md)
# Database
## FYI: The new artifact section will not show all of the files inside the artifact, only the ones I edited/created will be shown. If you want to see the whole file please click the repository link below.

## [See the Artifacts in the Repository](https://github.com/RanenHicks/ranenhicks.github.io/tree/main/Databases)

# Click to Navigate:
## [Old Artifact CS-340 Artifact Without Enhancements](#old-artifact)
* [RanenHicksProjectTwo.py](#ranenhicksprojecttwopy)
* [ProjectTwoDashboard - Ranen Hicks.ipynb](#projecttwodashboard---ranen-hicksipynb)

## [New Artifact CS-499 Artifact With Enhancements](#new-artifact)

[Back to Top](#click-to-navigate)
# Old Artifact:

[Back to Top](#click-to-navigate)
## ProjectTwoRanenHicks.py

```python
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, USER, PASS): #, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'aacPass'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31870
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# This method allows the user to insert an animal into the database
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary    
            return "True"  # Feedback to user.
        else:
            return "False"

# This method allows the user to search an AAC database for specific animals.
    def read(self, data):
        if data is not None:
            result = self.database.animals.find(data)  # Result stored in list.
            result2 = list(result)
            print("[")
            return result2
            print("]")
        
        else:
            print("[]") #Creating an empty list using brackets.
    
#  This method allows the user to update all queries that match their first input with what they want to change as their second.
    def update(self, data, data2):
        if data is not None:
                #  Only need to use update_many as it can do one and many updates. It also reduces the amount of code written.
                result = self.database.animals.update_many(data, data2)
                return result.modified_count
        else:
            return 0
    
#  This method allows the user to delete all the queries that match the input they entered into the funciton.
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data)
            return result.deleted_count
        else:
            return 0
```

[Back to Top](#click-to-navigate)
## ProjectTwoDashboard - Ranen Hicks.ipynb

```python
# Setup the Jupyter version of Dash
from jupyter_dash import JupyterDash

# Configure the necessary Python module imports for dashboard components
import dash_leaflet as dl
from dash import dcc
from dash import html
import plotly.express as px
from dash import dash_table
from dash.dependencies import Input, Output, State
import base64

# Configure OS routines
import os

# Configure the plotting routines
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#### FIX ME #####
# change animal_shelter and AnimalShelter to match your CRUD Python module file name and class name
from ProjectTwoRanenHicks import AnimalShelter

# The code I referenced will be cited in the readme.

###########################
# Data Manipulation / Model
###########################
# FIX ME update with your username and password and CRUD Python module name

username = "aacuser"
password = "aacPass"

# Connect to database via CRUD Module
db = AnimalShelter(username, password)

# class read method must support return of list object and accept projection json input
# sending the read method an empty document requests all documents be returned
df = pd.DataFrame.from_records(db.read({}))

# MongoDB v5+ is going to return the '_id' column and that is going to have an 
# invlaid object type of 'ObjectID' - which will cause the data_table to crash - so we remove
# it in the dataframe here. The df.drop command allows us to drop the column. If we do not set
# inplace=True - it will reeturn a new dataframe that does not contain the dropped column(s)
df.drop(columns=['_id'],inplace=True)

## Debug
# print(len(df.to_dict(orient='records')))
# print(df.columns)


#########################
# Dashboard Layout / View
#########################
app = JupyterDash(__name__)

#FIX ME Add in Grazioso Salvare’s logo
image_filename = 'Grazioso.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

#FIX ME Place the HTML image tag in the line below into the app.layout code according to your design
#FIX ME Also remember to include a unique identifier such as your name or date

app.layout = html.Div([
#    html.Div(id='hidden-div', style={'display':'none'}),
    
    html.Center(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))),
    html.Center(html.B(html.H1('CS-340 Dashboard - Ranen Hicks'))),
    html.Hr(),
    
    #FIXME Add in code for the interactive filtering options. For example, Radio buttons, drop down, checkboxes, etc.  
    html.Div([    
    dcc.Dropdown(['Reset', 'Water', 'Mountain or Wilderness', 'Disaster or Individual Tracking'], id='filter-type'),
    ]),   
    html.Hr(),
    dash_table.DataTable(id='datatable-id',
                         columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns],
                         data=df.to_dict('records'),
#FIXME: Set up the features for your interactive data table to make it user-friendly for your client
#If you completed the Module Six Assignment, you can copy in the code you created here 
                         
                         row_selectable = 'single',
                         sort_action = 'native',
                         sort_mode = 'multi',
                         filter_action = 'native',
                         selected_rows = [0],
                         page_size = 10,  # Page_size is 10 to allow the user to see the full list of one page without scrolling.

                        ),
    html.Br(),
    html.Hr(),
#This sets up the dashboard so that your chart and your geolocation chart are side-by-side
    html.Div(className='row',
         style={'display' : 'flex'},
             children=[
        html.Div(
            id='graph-id',
            className='col s12 m6',

            ),
        html.Div(
            id='map-id',
            className='col s12 m6',
            )
        ])
])

#############################################
# Interaction Between Components / Controller
#############################################



    
@app.callback(Output('datatable-id','data'),
              [Input('filter-type', 'value')])
def update_dashboard(value):
## FIX ME Add code to filter interactive data table with MongoDB queries    
    
    # Resets table
    if value == 'Reset':
        df = pd.DataFrame.from_records(db.read({}))
                                      
    # Sorts into correct breed and sex, however the age seems to not work correctly.
    elif value == 'Water':
        df = pd.DataFrame.from_records(db.read({"$or": [
            { "$and": [{'breed':'Labrador Retriever Mix', 'sex_upon_outcome': 'Intact Female',
                        'age_upon_outcome':{"$lte":'156'}, 'age_upon_outcome':{"$gte":'26'}}]},
            { "$and": [{'breed':'Chesapeake Bay Retriever', 'sex_upon_outcome': 'Intact Female',
                        'age_upon_outcome':{"$lte":'156'}, 'age_upon_outcome':{"$gte":'26'}}]},
            { "$and": [{'breed':'Newfoundland', 'sex_upon_outcome': 'Intact Female',
                        'age_upon_outcome':{"$lte":'156'}, 'age_upon_outcome':{"$gte":'26'}}]}]}))
        
    # Switches table to Mountain or Wilderness, this also has the age query problem. 
    elif value == 'Mountain or Wilderness':
        df = pd.DataFrame.from_records(db.read({"$or": [
            { "$and": [{'breed':'German Shepherd', 'sex_upon_outcome': 'Intact Male',
                        'age_upon_outcome':{"$lte":'156'}, 'age_upon_outcome':{"$gte":'26'}}]},
            { "$and": [{'breed':'Alaskan Malamute', 'sex_upon_outcome': 'Intact Male',
                        'age_upon_outcome':{"$lte":'156'}, 'age_upon_outcome':{"$gte":'26'}}]},
            { "$and": [{'breed':'Old English Sheepdog', 'sex_upon_outcome': 'Intact Male',
                        'age_upon_outcome':{"$lte":'156'}, 'age_upon_outcome':{"$gte":'26'}}]},
            { "$and": [{'breed':'Siberian Husky', 'sex_upon_outcome': 'Intact Male',
                        'age_upon_outcome':{"$lte":'156'}, 'age_upon_outcome':{"$gte":'26'}}]},
            { "$and": [{'breed':'Rottweiler', 'sex_upon_outcome': 'Intact Male',
                        'age_upon_outcome':{"$lte":'156'}, 'age_upon_outcome':{"$gte":'26'}}]}]}))
    
    # Switches table to Disaster or Individual Tracking, this also has the age query problem.
    elif value == 'Disaster or Individual Tracking':
        df = pd.DataFrame.from_records(db.read({"$or": [
            { "$and": [{'breed':'Doberman Pinscher', 'sex_upon_outcome': 'Intact Male',
                        'age_upon_outcome':{"$lte":'300'}, 'age_upon_outcome':{"$gte":'20'}}]},
            { "$and": [{'breed':'German Shepherd', 'sex_upon_outcome': 'Intact Male',
                        'age_upon_outcome':{"$lte":'300'}, 'age_upon_outcome':{"$gte":'20'}}]},
            { "$and": [{'breed':'Golden Retriever', 'sex_upon_outcome': 'Intact Male',
                        'age_upon_outcome':{"$lte":'300'}, 'age_upon_outcome':{"$gte":'20'}}]},
            { "$and": [{'breed':'Bloodhound', 'sex_upon_outcome': 'Intact Male',
                        'age_upon_outcome':{"$lte":'300'}, 'age_upon_outcome':{"$gte":'20'}}]},
            { "$and": [{'breed':'Rottweiler', 'sex_upon_outcome': 'Intact Male',
                        'age_upon_outcome':{"$lte":'300'}, 'age_upon_outcome':{"$gte":'20'}}]}]}))
            
            
            
    # Drops extra columns in the table and only leaves the new queried info for the table.
    df.drop(columns=['_id'],inplace=True)
    data=df.to_dict('records')
    
    return data

# Display the breeds of animal based on quantity represented in
# the data table
@app.callback(Output('graph-id', "children"),
              [Input('datatable-id', "derived_virtual_data")])


def update_graphs(viewData):
    
    ###FIX ME ####
    #add code for chart of your choice (e.g. pie chart) #
    
    # Creates an updated datafram when the table changes to also change the chart.
    dfnew = pd.DataFrame.from_dict(viewData)
    return [dcc.Graph(figure = px.pie(dfnew, names='breed', title='Preferred Animals'))]
    
#This callback will highlight a cell on the data table when the user selects it
@app.callback(Output('datatable-id', 'style_data_conditional'),
              [Input('datatable-id', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]


# This callback will update the geo-location chart for the selected data entry
# derived_virtual_data will be the set of data available from the datatable in the form of 
# a dictionary.
# derived_virtual_selected_rows will be the selected row(s) in the table in the form of
# a list. For this application, we are only permitting single row selection so there is only
# one value in the list.
# The iloc method allows for a row, column notation to pull data from the datatable
@app.callback(
    Output('map-id', "children"),
    [Input('datatable-id', "derived_virtual_data"),
     Input('datatable-id', "derived_virtual_selected_rows")])
def update_map(viewData, index):  
    if viewData is None:
        return
    elif index is None:
        return
    
    dff = pd.DataFrame.from_dict(viewData)
    # Because we only allow single row selection, the list can be converted to a row index here
    if index is None:
        row = 0
    else: 
        row = index[0]
        
    # Austin TX is at [30.75,-97.48]
    return [
        dl.Map(style={'width': '1000px', 'height': '500px'}, center=[30.75,-97.48], zoom=10, children=[
            dl.TileLayer(id="base-layer-id"),
            # Marker with tool tip and popup
            # Column 13 and 14 define the grid-coordinates for the map
            # Column 4 defines the breed for the animal
            # Column 9 defines the name of the animal
            dl.Marker(position=[dff.iloc[row,13],dff.iloc[row,14]], children=[
                dl.Tooltip(dff.iloc[row,4]),
                dl.Popup([
                    html.H1("Animal Name"),
                    html.P(dff.iloc[row,9])
                ])
            ])
        ])
    ]



app.run_server(debug=True)
```
[Back to Top](#click-to-navigate)
# New Artifact:

## ProjectTwoRanenHicks.py
```python
from pymongo import MongoClient
from bson.objectid import ObjectId 

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, USER, PASS): #, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacUser'
        #PASS = 'aacPass'
        # 
        # (Vlad, 2022; Installing / Upgrading, n.d.; premlatac87, 2024; kumarsar29u2, 2024; Doug_Duncan, 2022)
        HOST = 'localhost'
        PORT = 27017
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# This method allows the user to insert an animal into the database
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary 
            return "True"  # Feedback to user.
        else:
            return "False"

# This method allows the user to search an AAC database for specific animals.
    def read(self, data):
        if data is not None:
            result = self.database.animals.find(data)  # Result stored in list.
            result2 = list(result)
            print("[")
            return result2
            print("]")
        
        else:
            print("[]") # Creating an empty list using brackets.
    
# This method allows the user to update all queries that match their first input with what they want to change as their second.
    def update(self, data, data2):
        if data is not None:
                # Only need to use update_many as it can do one and many updates. It also reduces the amount of code written.
                result = self.database.animals.update_many(data, data2)
                return result.modified_count
        else:
            return 0
    
# This method allows the user to delete all the queries that match the input they entered into the funciton.
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data)
            return result.deleted_count
        else:
            return 0
```

## UpdateController.py:
```python
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
```

## models.py
```python
from django.db import models

# Create your models here.

# (AppSeed, 2022), creates a model that stores the structure of an animal object.
class AnimalModel(models.Model):
    age_upon_outcome = models.CharField(max_length = 100)
    animal_id = models.CharField(max_length = 100)
    animal_type = models.CharField(max_length = 100)
    breed = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100) 
    date_of_birth = models.CharField(max_length = 100)
    datetime = models.CharField(max_length = 100)
    mothyear = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    outcome_subtype = models.CharField(max_length = 100)
    outcome_type = models.CharField(max_length = 100)
    sex_upon_outcome = models.CharField(max_length = 100)
    location_lat = models.CharField(max_length = 100)
    location_long =  models.CharField(max_length = 100)
    age_upon_outcome_in_weeks =  models.CharField(max_length = 100)
```

## views.py
```python
from django.shortcuts import render

# (Mashutin, 2024; Writing Your First Django App, Part 1, n.d.), Renders the first database with button to datatable
def showLink(request):
    return render(request, "templates/homepage.html")
```

## urls.py(/database)
```python
from django.urls import path

from . import views

# (Mashutin, 2024; Writing Your First Django App, Part 1, n.d.)
urlpatterns = [
    path("", views.showLink, name = 'index'),
]
```
## citations.py
```python
# Author: Ranen Hicks
# Descriptionn: This program uses django to create a dynamic, filterable table on a webpage, and updates
# either mongoDB and SQLite database depending on user input. 
#
# Citations:
#
# aks. (2022, December 24). “no such table” exception (starball, Ed.). Stack Overflow. 
# https://stackoverflow.com/a/36453000
#
# anushka_jain_gfg. (2023, September 6). Convert Tuple to list in Python. GeeksforGeeks. 
# https://www.geeksforgeeks.org/convert-tuple-to-list-in-python/
#
# App Generator. (2023). app-generator/django-dynamic-datatb: Django Dynamic Datatables - Open-Source Library | AppSeed. GitHub. 
# https://github.com/app-generator/django-dynamic-datatb
#
# AppSeed. (2022, October 31). Django Dynamic Data Tables - Open-Source PYPI Library | AppSeed [Video]. YouTube. 
# https://www.youtube.com/watch?v=LlcpVfvIbMU
#
# Big McLargeHuge. (2019, March 11). How to open .SQLite files. Stack Overflow. 
# https://stackoverflow.com/a/55105501
#
# Clark, A. (2022, June 6). How to check if the string is empty in Python? (M. Ulhaq, Ed.). Stack Overflow.
# https://stackoverflow.com/a/9573259
#
# Doug_Duncan. (2022, September 13). Mongo/mongodb command not working and environment variable path is also set. MongoDB.
# https://www.mongodb.com/community/forums/t/mongo-mongodb-command-not-working-and-environment-variable-path-is-also-set/186599/2
#
# Easy Learning with HTML “Try it Yourself.” (n.d.). W3Schools. https://www.w3schools.com/html/default.asp
#
# GeeksforGeeks. (2023, August 28). Python  Convert a List into a  Tuple. GeeksforGeeks. 
# https://www.geeksforgeeks.org/python-convert-a-list-into-a-tuple/
# 
# Installing / Upgrading. (n.d.). PyMongo 4.8.0 Documentation. 
# https://pymongo.readthedocs.io/en/stable/installation.html
#
# kumarsar29u2. (2024, July 12). How to Find Out on Which Port MongoDB is Running. GeeksforGeeks. 
# https://www.geeksforgeeks.org/how-to-find-out-on-which-port-mongodb-is-running/
#
# Mashutin, D. (2024, July 15). How to connect Django with MongoDB | The PyCharm blog. The JetBrains Blog. 
# https://blog.jetbrains.com/pycharm/2024/01/how-to-connect-django-with-mongodb/
#
# premlatac87. (2024, June 26). How to Set Username and Password in MongoDB Compass. GeeksforGeeks. 
# https://www.geeksforgeeks.org/how-to-set-username-and-password-in-mongodb-compass/
#
# pulamolusaimohan. (2024, July 3). Python dict() Function. GeeksforGeeks. 
# https://www.geeksforgeeks.org/python-dict-function/
#
# Sanchithasr. (2022, September 24). 6 ways to convert a string to an array in JavaScript. DEV Community. 
# https://dev.to/sanchithasr/6-ways-to-convert-a-string-to-an-array-in-javascript-1cjg
#
# sqlite3 — DB-API 2.0 interface for SQLite databases. (2024, August 18). Python. 
# https://docs.python.org/3/library/sqlite3.html
#
# striver. (2024, July 5). Python String replace() Method. GeeksforGeeks. 
# https://www.geeksforgeeks.org/python-string-replace/
# 
# timonweb. (2020, March 30). Django is loading templates from a wrong directory. Django.
# https://forum.djangoproject.com/t/django-is-loading-templates-from-a-wrong-directory/1721/2
#
# unutbu. (2017, May 23). Python Sqlite3 - Data is not saved permanently (CommunityBot, Ed.). Stack Overflow.
# https://stackoverflow.com/a/26691539
#
# Vlad. (2012, June 6). ImportError: No module named objectid. Stack Overflow. https://stackoverflow.com/a/10919658
#
# Writing your first Django app, part 1. (n.d.). Django. https://docs.djangoproject.com/en/5.1/intro/tutorial01/
```

## settings.py
```python
"""
Django settings for CS499DatabasesRanenHicks project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-mdbh6*p$tsro7msyvy!av^7uracw%176&5qgdw4lr9+c55=gpx"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# (AppSeed, 2022; App Generator, 2023)
import django_dyn_dt

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # (AppSeed, 2022; App Generator, 2023)
    'django_dyn_dt', 
    'database'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "CS499DatabasesRanenHicks.urls"

# (timonweb, 2020; AppSeed, 2022; App Generator, 2023)
import os, inspect
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR_DATATB = os.path.join(BASE_DIR, "django_dyn_dt/templates")
TEMPLATE_DIR_DATABASE = os.path.join(BASE_DIR, "database/templates")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates"), TEMPLATE_DIR_DATATB, TEMPLATE_DIR_DATABASE], # (timonweb, 2020)
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "CS499DatabasesRanenHicks.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# (timonweb, 2020)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
         "NAME": BASE_DIR + "/db.sqlite3",
        }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# (AppSeed, 2022; App Generator, 2023)
DYN_DB_PKG_ROOT = os.path.dirname( inspect.getfile( django_dyn_dt ) )

STATICFILES_DIRS = (
    os.path.join(DYN_DB_PKG_ROOT, "templates/static"),
)

DYNAMIC_DATATB = {
    # SLUG -> Import_PATH 
    'AnimalShelterDatabase'  : "database.models.AnimalModel",
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
```

## urls.py (in /CS499DatabasesRanenHicks):
```python
"""
URL configuration for CS499DatabasesRanenHicks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    # (AppSeed, 2022; App Generator, 2023; Writing Your First Django App, Part 1, n.d.)
    path('', include("database.urls")),
    path('', include('django_dyn_dt.urls')),
]
```


