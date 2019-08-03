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

@app.route('/')
def index():
   return render_template("index.html")

@app.route("/predictor_map.html")
def maps():
    """Render Home Page."""
    return render_template("predictor_map.html")

@app.route("/cdc_data.html")
def cdc():
    """Render Home Page."""
    return render_template("cdc_data.html")

@app.route("/google_trends.html")
def google():
    """Render Home Page."""
    return render_template("google_trends.html")

@app.route("/contact.html")
def contact():
    """Render Home Page."""
    return render_template("contact.html")

if __name__ == '__main__':
   app.run(debug = True)