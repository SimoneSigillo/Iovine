#Crea un programma che scrive un file di testo che si chiama testo.txt e scrivi
#al suo interno 100 numeri casuali. Crea un altro programma che apre il file
#creato e restituisca a monitor i 100 numeri.

#leggiFile

f = open("testo.txt", 'r')

for riga in f:
    print(riga)

f.close()

    
