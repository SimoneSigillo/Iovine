#Chiedi all'utente il nome ed il cognome e restituisci in output il numero
#dei caratteri del nome e del cognome.
nome = str(input("Nome dell'utente: "))
cognome = str(input("Cognome dell'utente: "))

i = 0
j = 0
while i < len(nome):
    i = i + 1

while j < len(cognome):
    j = j + 1
    
print("La lunghezza del nome è di:",i, "caratteri")
print("La lunghezza del cognome è di:",j, "caratteri")

wait = input("Premi INVIO per continuare.")
