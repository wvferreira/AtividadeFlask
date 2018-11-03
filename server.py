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
    return render_template("dispersao.html")
@App.route("/graficodispersao", methods=["POST"])
def Dis():
    X = request.form["Coluna1"]
    Y = request.form["Coluna2"]
    sb.jointplot(x=X, y=Y, data=Dados)
    Mplt.savefig('C:\\Users\\guilh\\Downloads\\AtividadeFlask\\static\\img\\grafico.jpg')
    return render_template("teste.html",Coluna1=X,Coluna2=Y)

@App.route("/barras",methods=["GET"])
def Barras():
    return render_template("barras.html")


@App.route("/boxplot", methods=["GET"])
def Boxplot():
    return render_template("boxplot.html")
@App.route("/graficoboxplot", methods=["POST"])
def Box():
    Y = request.form["Coluna1"]
    sb.boxplot(y=Y, data=Dados)
    Mplt.savefig('C:\\Users\\guilh\\Downloads\\AtividadeFlask\\static\\img\\grafico.jpg')
    return render_template("teste.html",Coluna1=Y)

@App.route("/boxplotcat", methods=["GET"])
def Boxplotcat():
    return render_template("boxplotcat.html")
@App.route("/graficoboxplotcat", methods=["POST"])
def Boxplotcatg():
    X = request.form["Coluna1"]
    Y = request.form["Coluna2"]
    sb.boxplot(x=X, y=Y, data=Dados)
    Mplt.savefig('C:\\Users\\guilh\\Downloads\\AtividadeFlask\\static\\img\\grafico.jpg')
    return render_template("teste.html",Coluna1=X,Coluna2=Y)


@App.route("/histograma", methods=["GET"])
def Histograma():
    return render_template("histograma.html")
@App.route("/graficohistograma", methods=["POST"])
def Histo():
    X = request.form["Coluna1"]
    sb.distplot(Dados[X], bins=10 , kde=True)
    Mplt.savefig('C:\\Users\\guilh\\Downloads\\AtividadeFlask\\static\\img\\grafico.jpg')
    return render_template("teste.html",Coluna1=X)

if __name__ == "__main__":
    App.run(port=80,debug=80)