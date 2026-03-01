# Routes for OctoFit Tracker
from . import app

@app.route("/")
def home():
    return "Welcome to OctoFit Tracker!"