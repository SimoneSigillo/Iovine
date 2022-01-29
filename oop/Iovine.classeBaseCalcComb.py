# classe calcolo combinatorio

from itertools import permutations, combinations, combinations_with_replacement

class calcComb():

    def __init__(self, stringa):                                                                    # Il metodo costruttore inizializza le variabili dell'istanza, ossia rispettivamente
        self.__N = len(stringa)                                                                     # la lunghezza della stringa, la stringa, la lista delle lettere della stringa e la 
        self.__stringa = stringa                                                                    # lista degli anagrammi della stringa                            
        self.__listStringa = list(stringa)
        self.__anagrammi = self.anagrammi() 

    def getStringa(self):                                                                           # Fornisce la stringa inserita come istanza.
        return self.__stringa

    def getListStringa(self):                                                                       # Fornisce la lista delle lettere della stringa inserita come istanza.
        return self.__listStringa
    
    def setStringa(self, stringa):                                                                  # Permette di cambiare l'istanza con una nuova stringa.
        self.__stringa = stringa
        self.__N = len(stringa)
        self.__listStringa = list(stringa)
        self.__anagrammi = self.anagrammi()

    def charRipetuti(self):                                                                         # Fornisce un dictionary con le lettere come chiavi e il numero delle volte che il                                 
        carattere = {}                                                                              # carattere si presenta nella parola come valore e la lista dei valori.                                                                            
        for i in self.__listStringa:
            if (i in carattere):  # se trova il carattere nel dictionary incrementa il suo valore
                carattere[str(i)] += 1
            else:
                carattere[str(i)] = 1 # se non lo trova lo aggiunge
        ripetizioni = list(carattere.values())       
        variabiliRipetizioni = [carattere, ripetizioni]

        return variabiliRipetizioni

    
    def cerca(self):                                                                                # Controlla se la stringa inserita come istanza è presente nel vocabolario e quindi 
        f = open("word.italian.txt", 'r')                                                           # se ha senso compiuto.
        riga = f.readline()
        stringaPresente = False
        for riga in f:
            if self.__stringa == riga[:-1]:
                stringaPresente = True

        return stringaPresente

        
    def anagrammi(self):                                                                            # Fornisce la lista di anagrammi della stringa inserita come istanza.
        permutazioni = list(permutations(self.__listStringa))
        temp = ''
        anagrammi = []
        for i in permutazioni:
            for carattere in i:
                temp += carattere
            anagrammi.append(temp)
            temp = ''

        return anagrammi

    
    def confUtil(self):                                                                             # Fornisce la lista di anagrammi della stringa che hanno senso compiuto, servendosi   
        anagrammiValidi = []                                                                        # della lista di anagrammi e controllando che ognuno sia presente nel vocabolario  
        for i in self.__anagrammi:                                                                  # attraverso la funzione calcComb.cerca2().
            calcComb.cerca2(i)
            if  calcComb.cerca2(i) == True:
                anagrammiValidi.append(i)

        return anagrammiValidi

                     
    def cerca2(stringa):                                                                            # Serve per il funzionamento del modulo self.confUtil().
        f = open("word.italian.txt", 'r')
        riga = f.readline()
        stringaPresente = False
        for riga in f:
            if stringa == riga[:-1]:
                stringaPresente = True
        
        return stringaPresente 


    def fattoriale(n):                                                                              # Fornisce il fattoriale del numero inserito in input.
        if n < 0: 
            print("Il fattoriale di un numero negativo non esiste")

        elif n == 0: 
            return 1
        
        else: 
            fattoriale = 1
            while(n > 1): 
                fattoriale *= n 
                n -= 1
            return fattoriale


    def coeffBinom(n, k):                                                                           # Fornisce il coefficiente binomiale di due numeri inseriti in input.
        if k == n:
            return 1
        elif k == 1:         
            return n
        elif k > n:          
            return 0
        else:
            return calcComb.fattoriale(n) // (calcComb.fattoriale(k) * calcComb.fattoriale(n-k))
        


    # DISPOSIZIONI

    def nDispSempl(self, k):                                                                        # Fornisce il numero di disposizioni semplici.
        if self.__N >= k:
            nDispSempl = calcComb.fattoriale(self.__N) / calcComb.fattoriale(self.__N - k)

        return nDispSempl


    def nDispConRip(self, k):                                                                       # Fornisce il numero di disposizioni con ripetizione.
        nDispConRip = self.__N**k

        return nDispConRip


    def dispSempl(self, k):                                                                         # Fornisce la lista di disposizioni semplici.
        listaDispSempl = list(permutations(self.__listStringa, k))
        temp = ''
        dispSempl = []
        for i in listaDispSempl:
            for carattere in i:
                temp += carattere
            disposizioni.append(temp)
            temp = ''
        
        return dispSempl


    def dispConRip(self):
        pass



    # PERMUTAZIONI

    def nPermutSempl(self):                                                                         # Fornisce il numero di permutazioni semplici.
        nPermutSempl = calcComb.fattoriale(self.__N)

        return nPermutSempl


    def nPermutConRip(self):                                                                        # Fornisce il numero di permutazioni con ripetizione.
        denominatore = 1
        for i in range(0, len(self.charRipetuti()[1])):
            denominatore *= calcComb.fattoriale(self.charRipetuti()[1][i])
        nPermutConRip = calcComb.fattoriale(self.__N) / denominatore

        return nPermutConRip


    def permutSenzaRip(self):                                                                       # Fornisce la lista di permutazioni senza ripetizioni, che coincide con la lista 
        return self.anagrammi()                                                                     # di anagrammi


    def permutConRip(self):
        pass 



    # COMBINAZIONI

    def nCombSempl(self, k):                                                                        # Fornisce il numero di combinazioni semplici.
        nCombSempl = calcComb.fattoriale(self.__N) / (calcComb.fattoriale(k) * calcComb.fattoriale(self.__N-k))

        return nCombSempl


    def nCombConRip(self, k):                                                                       # Fornisce il numero di combinazioni con ripetizione.
        nCombConRip = calcComb.coeffBinom(self.__N+k-1, k)

        return nCombConRip


    def combSempl(self, k):                                                                         # Fornisce la lista di combinazioni semplici.
        listaCombSempl = list(combinations(self.__stringa, k))
        temp = ''
        combSempl = []
        for i in listaCombSempl:
            for carattere in i:
                temp += carattere
            combSempl.append(temp)
            temp = ''
        
        return combSempl


    def combConRip(self, k):                                                                        # Fornisce la lista di combinazioni con ripetizione.
        listaCombConRip = list(combinations_with_replacement(self.__stringa, k))
        temp = ''
        combSempl = []
        for i in listaCombConRip:
            for carattere in i:
                temp += carattere
            combConRip.append(temp)
            temp = ''
        
        return combConRip



    # PROBABILITA'

    def probConfUtil(self):                                                                         # Fornisce la probabilità che un'anagramma della parola inserita come istanza abbia 
        casiFavorevoli = 0                                                                          # senso compiuto.
        for i in self.__anagrammi: 
            Vtemp = calcComb.cerca2(i)
            if Vtemp == False:
                None
            elif Vtemp == True:
                casiFavorevoli += 1
        probabilità = casiFavorevoli/(len(self.__anagrammi))

        return probabilità
