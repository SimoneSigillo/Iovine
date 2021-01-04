#Il codice è stato rivisto rispetto a quello originale:
#ho eliminato le istruzioni non necessarie alla rappresentazione a cui volevo pervenire;
#non ho utilizzato il metodo readline poichè non leggeva tutte le righe del file di testo;
#non ho ordinto i valori delle coordinate.


import string
import numpy as np
import matplotlib.pyplot as plt

# apriamo il file in lettura
f = open("dati.txt", 'r')


# possiamo fare un ciclo e prendere riga per riga 

coordX = []
coordY = []

# da notare che posso fare un ciclo all'interno di un file
# direttamente sulle righe

i = 0
for riga in f:
    valori = str(riga)  # converto in stringa la riga (ho sostituito f.readline() con riga)
    valori = valori.strip('\n') # elimino il terminatore di riga
    valori = valori.split(',')  # separo la stringa in due numeri
    valori = list(valori)       # converto in lista
    print(valori)
    coordX.append(int(valori[0])) # aggiungo la coordinata X
    coordY.append(int(valori[1])) # aggiungo la coordinata Y
    i = i + 1


f.close()  # chiudiamo il file

print('Numero di coppie lette: ',i)

print ("X: ",coordX)
print ("Y: ",coordY)



# ora sono pronte per essere usate anche nei grafici

plt.scatter(coordX,coordY, c='g')
plt.title("GRAFICO A DISPERSIONE", c='r', fontsize=20)
plt.text(-15, -15, 'Ettore Iovine', fontsize=10)
plt.ylabel('y', loc='top', size=15, rotation=0)
plt.xlabel('x', loc='right', size=15)
plt.show()

