import string
import numpy as np
import matplotlib.pyplot as plt
from guizero import *

#ANDARE A GENERARE LE COPPIE DA SCRIVIFILE
coordX = []
coordY = []

f= open("dati.txt","r")

def coordinate ():
    for riga in f:
        valori = str(riga)  # converto in stringa la riga
        valori = valori.strip('\n') # elimino i lterminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        print(valori)
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y 

    output.append("X:")
    output.append(coordX)
    output.append("Y:")
    output.append(coordY)

def grafico ():
    for riga in f:
        valori = str(riga)  # converto in stringa la riga
        valori = valori.strip('\n') # elimino i lterminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        print(valori)
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y

    f.close()  

    plt.scatter(coordX,coordY,color='red', alpha=0.5, marker='.')
    plt.title("GRAFICO A DISPERSIONE", color='#003399')
    plt.grid()
    plt.ylabel('Y', color='#003399')
    plt.xlabel('X', color='#003399')
    plt.xticks([10*k for k in range(0,11)])
    plt.yticks([10*k for k in range(0,11)])
    plt.savefig("grafico.png")
    picture = Picture(app, image="grafico.png")

app= App(title="GRAFICO A DISPERSIONE", width=1200,height=1000, bg="#93C572")
etichetta = Text(app, text="INSERISCI IL NOME DEL FILE DA APRIRE: ", color="#B20000", size=30, font="helvetica")
nomefile = TextBox(app, width=100)
bottone1 = PushButton(app, text="GENERA LE COORDINATE", command=coordinate, args=[], width=40, height=4, align="top")
output = TextBox(app, width=100, height=15, multiline=True)
bottone = PushButton(app, text="GENERA IL GRAFICO", command=grafico, args=[], width=40, height=4, align="top")
bottone.bg = "#F5DEB3"
bottone1.bg = "#D2B48C"
app.display()
