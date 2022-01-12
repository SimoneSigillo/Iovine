# classe calcolo combinatorio

from itertools import permutations

class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)
        self.__anagrammi = anagrammi(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self, stringa):
        self.__stringa = stringa
        self.__N = len(stringa)
        self.__listStringa = list(stringa)
        self.__anagrammi = anagrammi(stringa)

    def charRipetuti(self):
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

        variabiliAnagrammi = [count, nCaratteri, carattere]

        return variabiliAnagrammi
    

    def cerca(self):
        f = open("word.italian.txt", 'r')
        riga = f.readline()
        stringaPresente == False
        for riga in f:
            if self.__stringa == riga[:-1]:
                stringaPresente == True
        f.close()

        return stringaPresente


    def fattoriale(n):
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
        if k == n:
            return 1
        elif k == 1:         
            return n
        elif k > n:          
            return 0
        else:
            return calcComb.fattoriale(n) // (calcComb.fattoriale(k) * calcComb.fattoriale(n-k))
            
    def anagrammi(self):
        #generiamo tutte le possibili permutazioni e le inseriamo in una lista
        permutazioni = list(itertools.permutations(self.__listStringa))

        #inizializiamo una variabile stringa di appoggio e una lista dove salvarle
        temp = ''
        anagrammi = []
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
        anagrammiPuliti = []
        for i in self.__anagrammi:
            calcComb.cerca(i)
            if stringaPresente == True:
                anagrammiPuliti.append(i)

        return anagrammiPuliti
                
            

        


    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        PermutSenzaRip = calcComb.fattoriale(self.__N)

        return PermutSenzaRip

    def nPermutConRip(self):
        PermutConRip = calcComb.fattoriale(self.__N) / calcComb.charRipetuti(self)

        return PermutConRip

    def permutSenzaRip(self):
        
        return calcComb.anagrammi(self)

    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self, k):
        if self.__N >= k:
            DispSemplSenzaRip = calcComb.fattoriale(self.__N) / calcComb.fattoriale(self.__N-k)

        return DispSemplSenzaRip

    def nDispSemplConRip(self, k):
        DispSemplConRip = self.__N**k

        return DispSemplConRip

    def dispSemplSenzaRip(self, k):
        listaDisposizioni = list(itertools.permutations(self.__stringa, k))
        temp = ''
        disposizioni = []
        for i in listaDisposizioni:
            for carattere in i:
                temp += carattere
            disposizoni.append(temp)
            temp = ''
        
        return disposizioni

    def dispSemplConRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici CON ripetizione
        '''
        return 0

    # COMBINAZIONI

    def nCombSemplSenzaRip(self, k):
        CombSemplSenzaRip = calcComb.fattoriale(self.__N) / (calcComb.fattoriale(k) * calcComb.fattoriale(self.__N-k))

        return CombSemplSenzaRip

    def nCombSemplConRip(self, k):
        CombSemplConRip = calcComb.coeffBinom(self.__N+k-1, k)

        return CombSemplConRip

    def combSenzaRip(self, k):
        listaCombinazioni = list(itertools.combinations(self.__stringa, k))
        temp = ''
        combinazioni = []
        for i in listaCombinazioni:
            for carattere in i:
                temp += carattere
            combinazioni.append(temp)
            temp = ''
        
        return combinazioni


    def combConRip(self):
        listaCombinazioni = list(itertools.combinations_with_replacement(self.__stringa, k))
        temp = ''
        combinazioni = []
        for i in listaCombinazioni:
            for carattere in i:
                temp += carattere
            combinazioni.append(temp)
            temp = ''
        
        return combinazioni

    # PROBABILITA'

    def probConfUtil(self):
        casiFavorevoli = 0
        for i in self.__anagrammi: 
            Vtemp = calcComb.confUtil(i)
            if Vtemp == False:
                None
            elif Vtemp == True:
                casiFavorevoli += 1
        
        probabilità = casifav/(len(self.__anagrammi))

        return probabilità
