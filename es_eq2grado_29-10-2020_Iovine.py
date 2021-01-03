i = str("s")
while i == str("s"):
    import math
    print ("Risolviamo l'equazione di 2° grado del tipo ax^2+bx+c=0")
    a = int(input("Inserisci il coefficiente a: "))
    b = int(input("Inserisci il coefficiente b: "))
    c = int(input("Inserisci il termine noto c: "))
    def secondogrado (a,b,c):
        if a == 0:
            x = -c/b
            print ("L'equazione immessa non è di 2° grado ma di 1° e la soluzione è:")
            print ("x =",x)
        elif b == 0:
            if c == 0:
                print ("L'equazione immessa è un'equazione di 2° grado monomia e ha come soluzioni:")
                print ("x1 = x2 = 0")
            else:
                print ("L'equazione immessa è un'equazione di 2° grado pura")
                xq = -c/a
                if xq < 0:
                    print ("L'equazione non ammette soluzioni")
                elif xq > 0:
                        print ("Le soluzioni sono:")
                        print ("x1 = +",math.sqrt(xq))
                        print ("x2 = -",math.sqrt(xq))
        elif c == 0:
            print ("L'equazione immessa è un'equazione di 2° grado spuria")
            print ("Le soluzioni sono:")
            print ("x1 = 0")
            print ("x2 = ",-b/a)
        else:
            print ("L'equazione immessa è un'equazione di 2° grado completa")
            delta = pow(b,2) - 4*a*c
            if delta < 0:
                print ("L'equazione non ammette soluzioni")
            elif delta == 0:
                print ("Ammette due soluzioni reali e coincidenti:")
                print ("x1 = x2 =",-b/2*a)
            else:
                print ("Le soluzioni sono:")
                print ("x1 = ",(-b-math.sqrt(delta))/2*a)
                print ("x2 = ",(-b+math.sqrt(delta))/2*a)


    secondogrado(a,b,c)

    i = str(input("Vuoi continuare? Se si premi [s] "))

   
                           
            
        
               
