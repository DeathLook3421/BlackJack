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
    
def plantar(mazoCasa, puntajeJ):
    puntajeCasa= sumarPuntaje(mazoCasa)
    print("LA CASA SIGUE JUGANDO")
    while (puntajeCasa<17):
        mazoCasa= mazoCasa+repartirCartas(1)
        puntajeCasa= sumarPuntaje(mazoCasa)
    if (puntajeCasa>21):
        print("¡LA CASA HA PERDIDO!")
    difCasa= 21-puntajeCasa
    difJugador=21-puntajeJ
    if difCasa>difJugador:
        print("¡EL JUGADOR HA GANADO!")
    elif difJugador>difCasa:
        print("¡LA CASA HA GANADO!")
        
    else:
        print("¡HA HABIDO UN EMPATE!")

def iniciarJuego():
    añadirCarta = 2
    print("\t ***BIENVENIDO A BLACK JACK*** \n\t     COMENCEMOS DE UNA VEZ")        
    cartasJugador= repartirCartas(2)
    mostrarCartasJ(cartasJugador)
    cartasCasa= repartirCartas(2)
    mostrarCartasC(cartasCasa)

    while(añadirCarta==2):
        puntajeJ=sumarPuntaje(cartasJugador)
        print("Tienes estos puntos: ", puntajeJ)
        print("Deseas plantarte o añadir otra carta, 1 para plantarte y 2 para añadir")
        añadirCarta = int(input())
        if añadirCarta==1:
            plantar(cartasCasa, puntajeJ)
            break
        cartasJugador= cartasJugador+ repartirCartas(1)
        mostrarCartasJ(cartasJugador)
        puntajeJ=sumarPuntaje(cartasJugador)
        if (puntajeJ>21):
            print("¡HAS PERDIDO!")
            break

iniciarJuego() 
