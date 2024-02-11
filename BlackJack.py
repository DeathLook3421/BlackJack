#random
from random import randint

pintas=["Picas","Treboles","diamantes","Corazones"]
valores=["A","J","Q","K"]+[str(i) for i in range(2,11)]

#for i in range()

letras={
    'K': 10,
    'Q': 10,
    'J': 10,
    'A': 1,
}

mazo=[(u,p) for u in valores for p in pintas]
mazoJ=['']
mazoC=['']

def dealer(a):

    for i in range(2):
        n=randint(0,51)
        #print(n)
        #print(mazo[n])
        a.extend(mazo[n])
        #print(mazoJ)
    return a

#def sumatoria():

#    suma=mazoJ[1]+mazoJ[3]
    #for i in range(2,2,n):
    #    print(a)

#    print("Suma que llevas: ",suma)

dealer(mazoJ)
print("Mazo del jugador: ",mazoJ[1:])

suma=(int(mazoJ[1])+int(mazoJ[3]))

print("Suma que llevas: ",suma)
#sumatoria(mazoJ)


dealer(mazoC)
print("Mazo de la casa: ",mazoC[1:3], " [OCULTA] ")
