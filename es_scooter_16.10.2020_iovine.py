giorni = int(input("Per quanti giorni vuoi noleggiare lo scooter? "))
costogiornouno = 45
costo = 40

if giorni == 1:
    print("Il costo per 1 giorno di noleggio è di",costogiornouno,"€")
elif giorni > 1:
    print("Il costo per",giorni,"giorni di noleggio è di",costo*giorni,"€")

wait = input("PREMI INVIO PER CONTINUARE.")
