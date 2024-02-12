from random import sample

letras= ["A", "J", "Q", "K" ] 
pintas = ["picas", "treboles", "diamantes", "corazones"]
valores = letras + [str(i) for i in range (2,11)]
mazo = [(v,p) for v in valores for p in pintas]


def repartirCartas(numCartas):
    mazoJugador = sample(mazo,numCartas)
    for carta in mazoJugador :
        mazo.remove(carta)
    return mazoJugador

def mostrarCartasJ(mazoJugador):
    print("Tus cartas son:\n", mazoJugador)
    
def mostrarCartasC(mazoCasa):    
    lenght = len(mazoCasa)
    cartasMostrar = []
    cartasMostrar.append(mazoCasa[0])
    for n in range(1,len(mazoCasa)):
        cartasMostrar.append(("*","*"))
    print("Las cartas de la casa son:\n",cartasMostrar)

def sumarPuntaje(mazo):
    suma=0
    for carta in mazo:
        if carta[0] in letras:
            suma += valorCartaL(carta)
        else:
            suma += int(carta[0])
    return suma        

def valorCartaL(carta):
    if carta[0]=="A":
        print("¿Cuánto deseas que valga el As? \t 1 o 11 \n ingrese el valor ")
        valorAs= input()
        return int(valorAs)
    return 10
    
cartasJugador= repartirCartas(2)
mostrarCartasJ(cartasJugador)
print("aslkdjaslkd", sumarPuntaje(cartasJugador))
cartasCasa= repartirCartas(2)
mostrarCartasC(cartasCasa)
print("dlaskjdlkasjd",sumarPuntaje(cartasCasa))
cartasJugador= cartasJugador+ repartirCartas(1)
mostrarCartasJ(cartasJugador) 
 
