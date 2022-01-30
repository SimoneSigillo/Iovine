# RUZZLE
### Indice
1. [Descrizione](#Descrizione)
2. [Interfaccia](#Interfaccia)
3. [Funzionalità](#Funzionalità)
4. [Caratteristiche tecniche](#Caratteristiche-tecniche)
***

## Descrizione
Ruzzle è un gioco interattivo online in cui l’obiettivo è quello di formare il maggior numero di parole con le lettere presenti nella griglia in un tempo prestabilito. Il punteggio dipenderà anche dalla lunghezza delle parole e dall’utilizzo di particolari caratteri.
Si svolgeranno 3 round al termine dei quali il vincitore sarà chi avrà totalizzato il punteggio maggiore.
***

## Interfaccia

***

## Funzionalità
All’avvio del gioco, viene chiesto di digitare il proprio nome utente, dopodichè si apre la schermata iniziale del gioco che propone le diverse modalità. Una volta scelta la modalità di gioco, occorre attendere il collegamento con un altro giocatore per avviare la partita.

#### Regole del gioco:
Il gioco si sviluppa in 3 manche, e il punteggio finale è dato dalla somma dei punteggi ottenuti nei singoli round. Ogni turno ha la durata di 2 min in cui il giocatore deve formare il maggior numero di parole di senso compiuto con le sedici lettere a disposizione nella griglia 4×4 sullo schermo. Le parole devono essere di almeno 2 lettere e non è possibile utilizzare la stessa casella-lettera più volte all’interno di una singola parola. Il valore di ogni parola è pari alla somma dei punti assegnati alle lettere di cui è composta, che variano in base alla difficoltà di poterle inserire nelle parole, e da eventuali moltiplicatori che verranno applicati se si utilizza la lettera su cui sono presenti. Inoltre vi sono diversi bonus assegnati una volta raggiunte determinate condizioni. 

##### Valore in punti di ogni lettera:
- 10 Punti:  J Q W X
- 8 Punti:  G H Z
- 5 Punti:  B D F K P V
- 4 Punti:  Y
- 3 Punti:  L M N U
- 2 Punti:  C R S T
- 1 Punto:  A E I O

##### Moltiplicatori:
- DL (Double Letter), duplica il valore della lettera;
- TL (Triple Letter), triplica il valore della lettere;
- DW (Double Word), duplica il valore della parola;
- TW (Triple Word), triplica il valore della parola.

##### Bonus:
- Lunghezza parola ≥ 5: 5 Punti
- Lunghezza parola ≥ 10: 30 Punti
- Primo a raggiungere 10 parole: 10 Punti nei primi due round, 20 Punti nel terzo round


Oltre alla classica, vi sono altre modalità che presentano diverse caratteristiche di gioco.

#### Modalità:
- lampo, 15 secondi ogni round;
- easy, griglia 6x6;
- hard, griglia 3x3;
- 1vs4: la partita si disputerà in 8 giocatori.

***
## Caratteristiche tecniche
Il codice del gioco è stato scritto seguendo una programmazione a oggetti.
### Programmazione a oggetti
La programmazione OOP (Object oriented Programming) "orientata agli oggetti", pone l’attenzione sui dati da manipolare, piuttosto che sulle procedure che li manipolano e impone che siano questi ultimi alla base del Modello Orientato ai Dati, un sistema costituito da un insieme di entità e oggetti che interagiscono tra loro. Il dato viene visto come un tipo di dato astratto caratterizzato da un insieme di valori che lo caratterizzano e da un insieme di operazioni che possono essere applicate a esso. E’ stata utilizzata la OOP poiché garantisce modularità e "riusabilità" del software, facile gestione e manutenzione di progetti di grandi dimensioni, riduce la dipendenza del programma dalla rappresentazione dei dati ai quali accede mediante un’interfaccia.
#### Classi e Oggetti
L’elemento principale della OOP è la classe, una descrizione astratta di un tipo di dato che descrive una famiglia di oggetti con caratteristiche e comportamenti simili. Un oggetto è un'istanza della classe, cioè la rappresentazione concreta di una classe. Quando si instanzia una variabile definendola di una classe si crea un oggetto di quella classe rappresentato dal nome della variabile istanziata. La differenza tra classe e oggetto è la stessa che c’è tra tipo di dato e dato. 
#### Attributi e Metodi
Una classe è costituita da attributi (campi che specificano le caratteristiche o proprietà che tutti gli oggetti della classe devono avere, i cui valori in un certo istante determinano lo stato del singolo oggetto della classe) e da Metodi (funzioni che specificano le azioni o i comportamenti ammissibili che un oggetto della classe è in grado di compiere; tali operazioni possono comunicare all’esterno lo stato dell’oggetto o modificarlo). I metodi di una classe sono l’Interfaccia della classe, l’unico strumento tramite il quale è possibile interagire con gli oggetti della classe.
Durante l’elaborazione un oggetto viene creato, utilizzato e infine distrutto. Gli oggetti di una classe vengono creati da uno specifico metodo Costruttore che deve avere lo stesso nome della classe che quando viene eseguito alloca la memoria necessaria a contenere l’oggetto e ne inizializza gli attributi. 
Nel nostro caso è stata creata la classe calcComb() che inizializza gli attributi dell’istanza e presenta come i moduli applicabili all’oggetto i modi per raggruppare e/o ordinare secondo date regole gli elementi di un insieme finito di oggetti, racchiusi nel Calcolo Combinatorio.

### Calcolo combinatorio
In definitiva il calcolo combinatorio fornisce quegli strumenti di calcolo per determinare il numero di raggruppamenti che si possono formare con un numero k di oggetti presi da un insieme contenente n oggetti (n ≥ k) secondo le modalità seguenti:
- i k oggetti possono formare gruppi ordinati ([disposizioni](#Disposizioni-semplici));
- se k = n otterremo dei gruppi ordinati ([permutazioni](#Permutazioni-semplici));
- i k oggetti possono formare gruppi non ordinati ([combinazioni](#Combinazioni-semplici)).

Esaminiamo in dettaglio questi raggruppamenti.

#### Disposizioni semplici
Si considera un insieme formato da n elementi distinti ed un numero k ≤ n. Si chiamano disposizioni semplici degli n elementi presi a k a k ( o disposizioni della classe k) un gruppo ordinato formato da k degli n elementi dell’insieme dato in modo che valgano le seguenti proprietà:
- in ciascun raggruppamento figurano k oggetti senza ripetizione;
- due di tali disposizioni si ritengono diverse quando differiscono per almeno un elemento oppure per l’ordine con cui gli stessi elementi si presentano.

Il numero delle disposizioni semplici di n elementi distinti della classe k, si indica con il simbolo D<sub>n, k</sub> il cui valore è uguale al prodotto di k numeri interi consecutivi decrescenti dei quali il primo è n.

Si ha cioè:

![disposizioni-semplici](https://github.com/ettoreiovine/Iovine/blob/main/oop/formulario/disposizioni_semplici.PNG)

Il simbolo n! si legge n fattoriale e non è altro che il prodotto di n numeri interi decrescenti a partire da n e per definizione si pone 0! = 1. Il suo calcolo è eseguito in uno dei metodi della classe calcComb().

#### Disposizioni con ripetizione
Si considera un insieme costituito da n elementi distinti ed un numero naturale k senza alcuna limitazione superiore. Il problema che si pone è quello di costruire tutti i possibili raggruppamenti distinti prendendo k oggetti in modo che:
- in ciascun raggruppamento figurano k oggetti ed uno stesso oggetto può figurare, ripetuto, fino ad un massimo di k volte;
- due qualsiasi raggruppamenti sono distinti se uno di essi contiene almeno un oggetto che non figura nell’altro, oppure gli oggetti sono diversamente ordinati, oppure gli oggetti che figurano in uno figurano anche nell’altro ma sono ripetuti un numero diverso di volte.

Il numero delle disposizioni con ripetizione si indica con il simbolo D’<sub>n, k</sub> e si dimostra che tale numero è dato da:

![disposizioni-con-ripetizione](https://github.com/ettoreiovine/Iovine/blob/main/oop/formulario/disposizioni_con_ripetizione.PNG)

#### Permutazioni semplici
Le permutazioni semplici altro non sono che le disposizioni di n oggetti presi ad n ad n. Ossia, dato un insieme di n oggetti, si dicono permutazioni di tali n oggetti tutti i gruppi che si possono formare con gli n oggetti dati prendendoli tutti. Se ne deduce allora che le permutazioni semplici differiscono soltanto per l’ordine con cui sono disposti gli n oggetti distinti contenuti nei vari raggruppamenti.
Dalla definizione segue quindi che le permutazioni coincidono con le disposizioni semplici di classe n, quindi il calcolo delle permutazioni è uguale al calcolo del numero delle disposizioni semplici di n elementi di classe n; quindi il numero delle permutazioni di n elementi distinti è uguale al prodotto dei primi n numeri naturali (escluso lo zero) ed è dato dal fattoriale del numero n, ossia:

![permutazioni-semplici](https://github.com/ettoreiovine/Iovine/blob/main/oop/formulario/permutazoni_semplici.PNG)

Gli anagrammi altro non sono che le permutazioni che si ottengono da una parola variando solo il posto delle lettere.

#### Permutazioni con ripetizione
Le permutazioni con ripetizione di n elementi, di cui h, k, … ripetuti, sono tutti i gruppi formati dagli n elementi, che differiscono per l’ordine in cui si presentano gli elementi distinti e la posizione che occupano gli elementi ripetuti:

![permutazioni-con-ripetizione](https://github.com/ettoreiovine/Iovine/blob/main/oop/formulario/permutazioni_con_ripetizione.PNG)
        
#### Combinazioni semplici
Dato un insieme di n elementi, si dicono combinazioni semplici degli n elementi presi a k a k (o di classe k) con k ≤ n tutti i gruppi di k elementi, scelti fra gli n dell’insieme dato, in modo che ciascun gruppo differisca dai restanti almeno per uno degli elementi in esso contenuti (senza
considerare, quindi, l’ordine degli elementi).
Da notare la differenza fra disposizioni e combinazioni (semplici): mentre nelle disposizioni si tiene conto dell’ordine, nelle combinazioni semplici, invece, si considerano distinti solo quando due i raggruppamenti differiscono almeno per un elemento. 
Per determinare il numero delle combinazioni semplici di n elementi di classe k, e che indichiamo con il simbolo C<sub>n, k</sub>, ci serviamo della formula:

![combinazioni-semplici](https://github.com/ettoreiovine/Iovine/blob/main/oop/formulario/combinazioni_semplici.PNG)


Il numero di combinazioni viene indicato anche con il simbolo ![simbolo-coefficiente-binomiale](https://github.com/ettoreiovine/Iovine/blob/main/oop/formulario/simbolo_coefficiente_binomiale.PNG), che si chiama coefficiente binomiale e si legge “n su k”.
Il coefficiente binomiale di due numeri n e k, con 0 ≤ k ≤ n, è il numero:

![coefficiente-binomiale](https://github.com/ettoreiovine/Iovine/blob/main/oop/formulario/coefficiente_binomiale.PNG)


#### Combinazioni con ripetizione
Considerando un insieme formato da n elementi e fissando un numero k (senza alcuna limitazione superiore), si costruiscono i possibili raggruppamenti distinti prendendo k elementi dell’insieme dato in modo che:
- ogni elemento può essere ripetuto al massimo fino a k volte;
- non interessa l’ordine con cui gli elementi si presentano;
- è diverso il numero di volte col quale un elemento compare.

La formula che dà il numero delle combinazioni con ripetizione di n elementi di classe k è:

![combinazioni-con-ripetizione](https://github.com/ettoreiovine/Iovine/blob/main/oop/formulario/combinazioni_con_ripetizione.PNG)

