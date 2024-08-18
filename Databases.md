<!-- (Github basic writing and formatting syntax, n.d.; jonikarppinen, 2019; Mendelssohn, 2022; Adding content to your GitHub Pages site using Jekyll, n.d.) -->

# Database
## [See the Artifacts in the Repository](https://github.com/RanenHicks/ranenhicks.github.io/tree/main/Databases)

# Click to Navigate:
## [Old Artifact CS-340 Artifact Without Enhancements](#old-artifact)
* [RanenHicksProjectTwo.py](#ranenhicksprojecttwopy)
* [ProjectTwoDashboard - Ranen Hicks.ipynb](#projecttwodashboard---ranen-hicksipynb)

## [New Artifact CS-499 Artifact With Enhancements](#new-artifact)

[Back to Top](#click-to-navigate)
# Old Artifact:

[Back to Top](#click-to-navigate)
## RanenHicksProjectTwo.py

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

