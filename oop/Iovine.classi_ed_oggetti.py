class auto:

    # Attributi di Classe
    garanzia = 1
    assicurazione = True
    parcoAuto = 0

    #Metodo costruttore
    def __init__(self,proprietario, marca, modello, cilidrata, cavalli, colore):

        # Attributi di Istanza
        self.proprietario = proprietario
        self.marca = marca
        self.modello = modello
        self.cilindrata = cilidrata
        self.cavalli = cavalli
        self.colore = colore
        
        auto.parcoAuto +=1

    #Metodo di tipo Get
    def scheda(self):
        return f'\nScheda "{self.proprietario}"\n Marca: {self.marca}\n Modello: {self.modello}\n Cilindrata: {self.cilindrata}\n Cavalli: {self.cavalli}\n colore: {self.colore}\n assicurazione: {self.assicurazione}' 

    #Metodo tipo Set
    def cambiaAttributo(self):
        attributoDaCambiare = input("Inserisci l'attributo che vuoi cambiare:" )
        self.attributoDaCambiare = input("Inserisci il nuovo attributo: ")
        
giovanni = auto("giovanni","ford","fiesta",1500, 160, "rosso")

marco = auto("marco","fiat","Bravo",2500, 200, "verde")

print("Il tipo di variabile costruita è:")
print(giovanni)
print(marco)

giovanni.cambiaAttributo()

print("\nLa singola scheda è:")
print (giovanni.scheda())
print (marco.scheda())
print("\nauto totali: ",auto.parcoAuto)

print("\n\naltro metodo per visualizzare le informazioni (__dict__):")

print(giovanni.__dict__)
print(marco.__dict__)




