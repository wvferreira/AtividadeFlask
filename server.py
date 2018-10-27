from flask import Flask
from flask import render_template
import pandas as pd
from matplotlib import pyplot as Mplt
import seaborn as sb
from flask import request

App = Flask (__name__)
Dados = pd.read_excel('C:\\Users\\guilh\\Downloads\\AtividadeFlask\\Planilha\\PesquisaAuto.xlsx', delimiter=',')

@App.route("/", methods=["GET"])
@App.route("/home", methods=["GET"])
def Home():
    return render_template("home.html")

@App.route("/dispersao", methods=["GET"])
def Dispersão():
    Coluna1 = request.form["Coluna1"]
    Coluna2 = request.form["Coluna2"]
    return render_template("dispersao.html",Coluna1=Coluna1 , Coluna2=Coluna2 )

@App.route("/barras", methods=["GET"])
def Barras():
    return render_template("barras.html")

@App.route("/boxplot", methods=["GET"])
def Boxplot():
    return render_template("boxplot.html")

@App.route("/boxplocat", methods=["GET"])
def Boxplotcat():
    return render_template("boxplocat.html")

@App.route("/histograma", methods=["GET"])
def Histograma():
    return render_template("histograma.html")

if __name__ == "__main__":
    App.run(port=80,debug=80)