#Crea una lista bidimensionale di numeri casuali,tre righe per tre colonne e
#chiedi all'utente quale riga vuole visualizzare.

from random import randint

array = [[randint(1,100) for x in range(3)],
         [randint(1,100) for x in range(3)],
         [randint(1,100) for x in range(3)]]
for i in range(0,3):
    print(array[i])

scelta = int(input("Quale riga vuoi visualizzare? "))
print(array[scelta])

             
