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
    #Coluna1 = request.form["Coluna1"]
    #Coluna2 = request.form["Coluna2"]
    return render_template("dispersao.html")

@App.route("/barras", methods=["GET"])
def Barras():
    #GraficoBarras()
    return render_template("barras.html")

@App.route("/boxplot", methods=["GET"])
def Boxplot():
    #GraficoBox()
    return render_template("boxplot.html")

@App.route("/boxplocat", methods=["GET"])
def Boxplotcat():
    #GraficoBoxCat()
    return render_template("boxplocat.html")



@App.route("/histograma", methods=["GET"])
def Histograma():
    return render_template("histograma.html")
@App.route("/gravar", methods=["POST"])
def Histo():
    X = request.form["Coluna1"]
    sb.distplot(Dados[X], bins=10 , kde=True)
    Mplt.savefig('C:\\Users\\guilh\\Downloads\\AtividadeFlask\\static\\img\\histograma1.jpg')
    return render_template("teste.html",Coluna1=X)
@App.route("/teste", methods=["GET"])
def testando():
    return render_template("teste.html")



if __name__ == "__main__":
    App.run(port=80,debug=80)