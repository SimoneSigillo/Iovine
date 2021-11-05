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

    def setStringa(self):
        '''
        modificare questo metodo in modo da verificare la coerenza delle variabili di
        istanza presenti
        '''
        
        return 0

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

    def coeffBinom(n, k):
        ''' 
        implementare la formula del coefficiente binomiale a partire dal fattoriale
        '''
        pass

                
        
        


    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        '''
        restituire il numero di permutazioni SENZA ripetizione
        '''
        PermutSenzaRip = math.factorial(self.__N)

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
            DispSemplSenzaRip = math.factorial(self.__N) / math.factorial(self.__N-k)

        return DispSemplSenzaRip

    def nDispSemplConRip(self, k):
        '''
        restituire il numero di disposizioni semplici CON ripetizione
        '''
        DispSemplConRip =self.__N **k

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
        CombSemplSenzaRip = math.factorial(self.__N) / (math.factorial(k) * math.factorial(self.__N-k))

        return CombSemplSenzaRip

    def nCombSemplConRip(self, k):
        '''
        restituire il numero delle combinazioni CON ripetizione
        '''
        CombSemplConRip = math.factorial(self.__N+k-1) / (math.factorial(k) * math.factorial(self.__N-1))

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


