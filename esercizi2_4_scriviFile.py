#Crea un programma che scrive un file di testo che si chiama testo.txt e scrivi
#al suo interno 100 numeri casuali. Crea un altro programma che apre il file
#creato e restituisca a monitor i 100 numeri.

#scriviFile

from random import randint

f = open("testo.txt", 'w')

dati = ""

for riga in range(100):
    for elemento in range(1):
        dati = dati + str(randint(1,100))
        dati = dati + "\n"


f.write(dati)

f.close()
