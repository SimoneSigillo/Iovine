# classe calcolo combinatorio

class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self, stringa):
        '''
        modificare questo metodo in modo da verificare la coerenza delle variabili di
        istanza presenti
        '''
        self.__stringa = stringa
        return self.__stringa

    def charRipetuti(self):
        '''
        questo metodo deve creare un dictionary all'interno del quale la chiave deve essere
        il singolo carattere, il valore deve essere il numero di ripetizioni di quel carattere
        esempi di dictionary sono presenti nel file elementi_base/dictionary.py
        '''

    def confUtil(self):
        '''
        verificare se la STRINGA attributo di istanza è presente
        nel file word.italian.txt 
        '''
        f = open("word.italian.txt", 'r')
        riga = f.readline()
        stringaPresente == False
        for riga in f:
            if self.__stringa == riga[:-1]:
                stringaPresente == True
        f.close()

        return stringaPresente

    def fattoriale(n):
        '''
        implementare una qualunque versione della funzione fattoriale
        '''
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

    def coeffBinom(n, k):
        ''' 
        implementare la formula del coefficiente binomiale a partire dal fattoriale
        '''
        
        if k == n:
            return 1
        elif k == 1:         
            return n
        elif k > n:          
            return 0
        else:
            return calcComb.fattoriale(n) // (calcComb.fattoriale(n) * calcComb.fattoriale(n-k))
            

        
        


    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        '''
        restituire il numero di permutazioni SENZA ripetizione
        '''
        PermutSenzaRip = calcComb.fattoriale(self.__N)

        return PermutSenzaRip

    def nPermutConRip(self):
        '''
        restituire il numero di permutazioni CON ripetizione
        '''
        return 0

    def permutSenzaRip(self):
        '''
        generare e restituire la lista di permutazioni SENZA ripetizione
        '''
        return 0

    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self, k):
        '''
        restituire il numero di disposizioni semplici SENZA ripetizione
        '''
        if self.__N >= k:
            DispSemplSenzaRip = calcComb.fattoriale(self.__N) / calcComb.fattoriale(self.__N-k)

        return DispSemplSenzaRip

    def nDispSemplConRip(self, k):
        '''
        restituire il numero di disposizioni semplici CON ripetizione
        '''
        DispSemplConRip = self.__N**k

        return DispSemplConRip

    def dispSemplSenzaRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici SENZA ripetizione
        '''
        return 0


    def dispSemplConRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici CON ripetizione
        '''
        return 0

    # COMBINAZIONI

    def nCombSemplSenzaRip(self, k):
        '''
        restituire il numero delle combinazioni SENZA ripetizione
        '''
        CombSemplSenzaRip = calcComb.fattoriale(self.__N) / (calcComb.fattoriale(k) * calcComb.fattoriale(self.__N-k))

        return CombSemplSenzaRip

    def nCombSemplConRip(self, k):
        '''
        restituire il numero delle combinazioni CON ripetizione
        '''
        CombSemplConRip = calcComb.fattoriale(self.__N+k-1) / (calcComb.fattoriale(k) * calcComb.fattoriale(self.__N-1))

        return CombSemplConRip

    def combSenzaRip(self):
        '''
        generare e restituire la lista delle combinazioni SENZA ripetizione
        '''
        return 0


    def combConRip(self):
        '''
        generare e restituire la lista delle combinazioni CON ripetizione
        '''
        return 0


