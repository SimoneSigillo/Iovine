#Chiedi all'utente il suo colore preferito, se digita: “rosso”, “Rosso”
#o “ROSSO” rispondi “bello” altrimenti rispondi “non mi piace”.
colore = str(input("Qual è il tuo colore preferito? "))
if colore == "rosso" and "Rosso" and "ROSSO":
    print("Bello")
else:
    print("Non mi piace")

wait = input("Premi INVIO per continuare.")
