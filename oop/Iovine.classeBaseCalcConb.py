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

    def confUtil(self):
        '''
        verificare se la STRINGA attributo di istanza è presente
        nel file word.italian.txt 
        '''
        f = open("word.italian.txt", 'r')
        stringaPresente == False
        for riga in f:
            if self.__stringa in riga:
                stringaPresente == True
        f.close()

        return stringaPresente
                
        
        


    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        '''
        restituire il numero di permutazioni SENZA ripetizione
        '''
        n = len(self.__stringa)
        PermutSenzaRip = math.factorial(n)

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

    def nDispSemplSenzaRip(self):
        '''
        restituire il numero di disposizioni semplici SENZA ripetizione
        '''
        n = len(self.__stringa)
        if n >= k:
            DispSemplSenzaRip = math.factorial(n) / math.factorial(n-k)

        return DispSemplSenzaRip

    def nDispSemplConRip(self):
        '''
        restituire il numero di disposizioni semplici CON ripetizione
        '''
        n = len(self.__stringa)
        DispSemplConRip = n**k

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

    def nCombSemplSenzaRip(self):
        '''
        restituire il numero delle combinazioni SENZA ripetizione
        '''
        n = len(self.__stringa)
        CombSemplSenzaRip = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

        return CombSemplSenzaRip

    def nCombSemplConRip(self):
        '''
        restituire il numero delle combinazioni CON ripetizione
        '''
        n = len(self.__stringa)
        CombSemplConRip = math.factorial(n+k-1) / (math.factorial(k) * math.factorial(n-1))

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


