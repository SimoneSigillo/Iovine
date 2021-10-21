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
        for riga in f:
            if self.__stringa in riga:
                print("La stringa ", self.__stringa, " ha un significato compiuto.")
        f.close()
                
        
        


    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        '''
        restituire il numero di permutazioni SENZA ripetizione
        '''
        n = len(self.__stringa)
        permutazioni = math.factorial(n)
        print("Il numero i permutazioni è ",permutazioni)

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
            disposizioni = math.factorial(n) / math.factorial(n-k)
            print("Il numero di disposizioni semplici è ", disposizioni)
        else:
            print("k non può essere maggiore di n nelle disposizioni semplici")

    def nDispSemplConRip(self):
        '''
        restituire il numero di disposizioni semplici CON ripetizione
        '''
        n = len(self.__stringa)
        disposizioni = n**k
        print("Il numero di disposizioni con ripetizione è ", disposizioni)

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
        combinazioni = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
        print("Il numero di combinazioni semplici è ", combinazioni)

    def nCombSemplConRip(self):
        '''
        restituire il numero delle combinazioni CON ripetizione
        '''
        n = len(self.__stringa)
        combinazioni = math.factorial(n+k-1) / (math.factorial(k) * math.factorial(n-1))
        print("Il numero di combinazioni con ripetizione è ", combinazioni)

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


