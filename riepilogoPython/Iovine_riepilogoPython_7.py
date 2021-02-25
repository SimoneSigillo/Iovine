#Chiedi all'utente il suo nome e restituisci in output tutte le lettere del nome,
#una alla volta.
nome = str(input("Nome dell'utente: "))
i = 0
while i < len(nome):
    print(nome[i])
    i = i + 1
