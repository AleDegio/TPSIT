"""
Alessia De Giovannini
Cifrario di Vernam 
(lettere alfabeto con lettere straniere)
"""
#creo una variabile alfabeto 
#per associare ad ogni lettere un numero (A=0,...) 
#attraverso il metodo alfabeto.index("A") 
#(restiuisce 0 essendo A la prima lettera)
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#converte la parola e la chiave 
#nel corrispettivo valore numero 
#in base all'alfabeto
def fromStringToInt(parola, chiave):
    parola = parola.upper()
    chiave = chiave.upper()
    intParola = []
    intChiave = []

    #converto le lettere della parola in numeri A = 0 ecc.
    for i in range(0, len(parola)):
        intParola.append(alfabeto.index(parola[i])) #alfabeto.index restituisce l'index in cui è stato trovato il carattere 

    #converto le lettere della chiave in numeri A = 0 ecc.
    for i in range(0, len(chiave)):
        intChiave.append(alfabeto.index(chiave[i]))
    
    return intParola, intChiave #vettori di interi

#funzione inversa a fromStringToInt 
#dato un intero lo converte nel carattere corrispettivo 
#in base alla posizione nell'alfabeto
def fromIntToString(somma):
    parolaCifrata = []
    for i in range(0,len(somma)):
        parolaCifrata.append(alfabeto[somma[i]])
    
    return parolaCifrata


def cifra(parola, chiave):
    intParola, intChiave = fromStringToInt(parola,chiave)
    somma = []
    min = 0

    #effettuo la somma
    #trovo il vettore più piccolo così so quanti numeri devo sommare 
    #(es. intParola = {1,2,3} intChiave = {4,5,6,7}, sommo solo 1+4 2+5 3+6) 
    if len(intParola) < len(intChiave): 
        min = len(intParola)
    else:
        min = len(intChiave)
    
    for i in range(0, min):
        somma.append(intParola[i] + intChiave[i]) #creo vettore delle somme

    #effettuo il modulo
    for i in range(0, min):
        somma[i] = somma[i] % 26    #effettuo il mod 26 su ogni elemento del vettore

    parolaCifrata = fromIntToString(somma) #riconverto il tutto in caratteri in base alla posizione dell'alfabeto
    return parolaCifrata
    
def main():
    #chiedo parola e chiave
    parola = input("Inserisci la parola da cifrare: ")
    chiave = input("Inserisci la chiave di cifratura: ")
    parolaCifrata = cifra(parola,chiave)

    print(parolaCifrata)

if __name__ == "__main__":
    main()