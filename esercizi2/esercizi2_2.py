#Costruisci un Array con 5 numeri casuali compresi fra 1 e 8.
#Fai scegliere all'utente uno dei numeri dell'array e restituisci in output il
#numero di volte che si ripete il numero scelto.

import numpy as np
import random

lista = []

a = 0
while a < 5:
    b = random.randint(1,8)
    lista = lista + [b]
    a = a + 1

array = np.array([lista])
print(array)

scelta = int(input("Scegli uno dei numeri dell'array: "))

i = 0
r = 0
while i < 5:
    if lista[i] == scelta:
        r = r + 1
    i = i + 1
        
if r == 1:
    print("Il numero",scelta,"si ripete",r,"volta")
else: 
    print("Il numero",scelta,"si ripete",r,"volte")
