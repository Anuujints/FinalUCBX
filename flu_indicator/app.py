import os
import io
import numpy as np

import keras
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from keras.applications.xception import (
    Xception, preprocess_input, decode_predictions)
from keras import backend as K

from flask import Flask, request, redirect, url_for, jsonify, render_template

app = Flask(__name__)

# Route to Homepage
@app.route('/')
def index():
   return render_template("index.html")

# Route to Maps page in Explore tab
@app.route("/predictor_map.html")
def maps():
    """Render Home Page."""
    return render_template("predictor_map.html")

# Route to Weekly Influenza Predictor
@app.route("/weekly_predictor.html")
def predictor():
    """Render Home Page."""
    return render_template("weekly_predictor.html")

# Route to CDC Data
@app.route("/cdc_data.html")
def cdc():
    """Render Home Page."""
    return render_template("cdc_data.html")

# Route to Google Trends 
@app.route("/google_trends.html")
def google():
    """Render Home Page."""
    return render_template("google_trends.html")

# Route to Similar Studies
@app.route("/studies.html")
def studies():
    """Render Home Page."""
    return render_template("studies.html")

# Route to Contact page
@app.route("/contact.html")
def contact():
    """Render Home Page."""
    return render_template("contact.html")

if __name__ == '__main__':
   app.run(debug = True)