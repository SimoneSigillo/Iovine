import string
import numpy as np
import matplotlib.pyplot as plt
from guizero import *

coordX = []
coordY = []

f= open("dati.txt","r")

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

    print ("X: ",coordX)
    print ("Y: ",coordY)

    plt.scatter(coordX,coordY,color='red', alpha=0.5, marker='.')
    plt.title("GRAFICO A DISPERSIONE", color='#003399')
    plt.ylabel('Y', color='#003399')
    plt.xlabel('X', color='#003399')
    plt.xticks([10*k for k in range(0,11)])
    plt.yticks([10*k for k in range(0,11)])
    plt.savefig("grafico.png")
    picture = Picture(app, image="grafico.png")

app= App(title="GRAFICO A DISPERSIONE", width=2000,height=2000, bg="#93C572")
etichetta = Text(app, text="INSERISCI IL NOME DEL FILE DA APRIRE: ", color="#B20000", size=30, font="helvetica")
nomefile = TextBox(app, width=100)
bottone = PushButton(app, text="GENERA IL GRAFICO", command=grafico, args=[],width=50, height=5)
bottone.bg = "#F5DEB3"
app.display()
