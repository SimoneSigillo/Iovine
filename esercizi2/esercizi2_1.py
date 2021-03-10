#Chiedi all'utente una lista di 5 numeri interi e salvali in un Array.
#Ordina la lista e restituiscila in output nell'ordine inverso.

import numpy as np

n1 = int(input("Inserisci primo numero intero: "))
n2 = int(input("Inserisci secondo numero intero: "))
n3 = int(input("Inserisci terzo numero intero: "))
n4 = int(input("Inserisci quarto numero intero: "))
n5 = int(input("Inserisci quinto numero intero: "))

lista = [n1, n2, n3, n4, n5]

array = np.array([n1,n2,n3,n4,n5])

lista.sort()

lista.reverse()

print(lista)
