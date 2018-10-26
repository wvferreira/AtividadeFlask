from flask import Flask
from flask import render_template
import pandas as pd
from matplotlib import pyplot as Mplt
import seaborn as sb

App = Flask (__name__)

@App.route("/", methods=["GET"])
@App.route("/home", methods=["GET"])
def Home():
    return render_template("home.html")