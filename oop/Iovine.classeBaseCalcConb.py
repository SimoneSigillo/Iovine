# classe calcolo combinatorio

class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)
        self.__anagrammi = anagrammi(self.__stringa)

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
        carattere = {}
        nCaratteri = 0
        count = 0
        for i in self.__listStringa:
            if (i in carattere):  # se trova il carattere nel dictionary incrementa il suo valore
                carattere[str(i)] += 1
            else:
                carattere[str(i)] = 1 # se non lo trova lo aggiunge
        for i in carattere:
            if carattere[i]>1: # se trova una lettera ripetuta
                count += 1 # incrementa il numero di caratteri che si ripetono
                nCaratteri += carattere[i] # incrementa il numero totale di ripetizioni

        return carattere
    

    def cerca(self):
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
            return calcComb.fattoriale(n) // (calcComb.fattoriale(k) * calcComb.fattoriale(n-k))
            
    def anagrammi(self):
        '''
        a partire dalla stringa (caratterizzante l'oggetto) si restituisca la lista di tutti
        gli anagrammi possibili. E' presente uno script nel repo che esegue questo compito.
        '''
        from itertools import permutations

        '''
        Il seguente script genera una lista di anagrammi a partire da una stringa di caratteri data
        '''
        #generiamo tutte le possibili permutazioni e le inseriamo in una lista
        permutazioni = list(permutations(self.__listStringa))

        #inizializiamo una variabile stringa di appoggio e una lista dove salvarle
        temp = ''
        anagrammi = []

        '''
         il metodo permutations genera una lista di tuple, ognu tupla è una permutazione.
         se scorriamo la lista attraverso un ciclo, possiamo scorrere gli elementi della tupla
         per ricostruire la stringa
        '''
        for i in permutazioni:
            for carattere in i:
                # in temp concateno tutti gli elementi della tupla così da
                # ottenere i singoli anagrammi della stringa iniziale
                temp += carattere 

            # aggiungo la parola ricostruita dalla tupla alla lista finale degli anagrammi
            anagrammi.append(temp)
            # "svuoto" la variabile temp così da ricostruire un secondo anagramma
            temp = ''

        return anagrammi

    def confUtil(self):
        '''
        confUtil mette insieme diversi metodi basilari, lo scopo è:
        a partire dalla lista di tutti gli anagrammi, verifica parola per parola la sua
        presenza all'interno del file delle parole di senso compiuto, cancellando le altre.
        si consiglia l'utilizzo di anagrammi e cerca, presenti nel repo e da trasformare in metodi.
        è possibile in una seconda versione la ricefrca di parole in altre lingue. 
        '''

        anagrammiPuliti = []
        for i in self.__anagrammi:
            calcComb.cerca(i)
            if stringaPresente == True:
                anagrammiPuliti.append(i)

        return anagrammiPuliti
                
            

        


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
        from itertools import permutations

        permutazioni = list(permutations(self.__listStringa))
        return permutazioni

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
        CombSemplConRip = calcComb.coeffBinom(self.__N+k-1, k)

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

    # PROBABILITA'

    def probConfUtil(self):
        pass

