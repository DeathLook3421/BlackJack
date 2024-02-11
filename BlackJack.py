#random
from random import randint

pintas=["Picas","Treboles","diamantes","Corazones"]
valores=["A","J","Q","K"]+[str(i) for i in range(2,11)]

letras={'J':10,'Q':10,'K':10,'A':1}
suma=sum(letras.get(x, x) for x in letras)

#Intento 1 de convertir las letras a numeros
#for i in range(len(valores)):
#    if valores[i] in ["J", "K","Q"]:
#        valores[i]=10

#for i in range(len(valores)):
#    if valores[i] in ["A"]:
#        valores[i]=1

#Intento 2 de convertir las letras a numeros
#letras={
#    'K': 10,
#    'Q': 10,
#    'J': 10,
#    'A': 1,
#}

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

#intento 3 de convertir las letras a numeros
#def sumatoria(a):
#    suma=0
#    for i in range(1,n,2):
#        suma=a[i]
#    print("Suma que llevas: ",suma)

dealer(mazoJ)
print("Mazo del jugador: ",mazoJ[1:])

suma=(int(mazoJ[1])+int(mazoJ[3]))

print("Suma que llevas: ",suma)
#sumatoria(mazoJ)


dealer(mazoC)
print("Mazo de la casa: ",mazoC[1:3], " [OCULTA] ")
