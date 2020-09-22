# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Import SQL Alchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import dependencies for Flask
from flask import Flask, jsonify

# Set up engine
engine = create_engine("sqlite:///hawaii.sqlite")

# Define classes
Base = automap_base()

# Reflect the database
Base.prepare(engine, reflect=True)
# Reference classes/tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link
session = Session(engine)

# Define Flask app
app = Flask(__name__)

# Define routes
@app.route("/")
def welcome():
    return(
        '''
        Welcome to the Climate Analysis API
        Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api./v1.0/temp/start/end
        ''')