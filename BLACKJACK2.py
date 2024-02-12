from random import sample
print(" BIENVENIDO A BLACKJACK ")

pintas = ["picas", "treboles", "diamantes", "corazones"]
valores = ["A", "J", "Q", "K" ] + [str(i) for i in range (2,11)]
mazo = [(v,p) for v in valores for p in pintas]
mazoJugador=[]
mazoCasa=[]

def suma_total(turn):
    suma_t = 0
    for carta in turn:
        if carta[0] in ["Q", "K", "J"]:
            suma_t += 10
        elif carta[0] == "A":
            if suma_t + 11<=21:
                 suma_t += 11
            else:
                 suma_t += 1
        else: 
            suma_t += int(carta[0])
    return suma_t

def inicioJuego():
    mazoJugador = sample(mazo,2)
    for carta in mazoJugador :
        mazo.remove(carta)
    return mazoJugador
 
def juego_casa(cartasCasa):
    while suma_total(cartasCasa)<= 16:
        add_carta= sample(mazo,1)[0]
        cartasCasa.append (add_carta)
        mazo.remove(add_carta)
    suma_casa=suma_total(cartasCasa)
    return cartasCasa

cartasJugador = inicioJuego()
print("Tus cartas son: ", cartasJugador, " para un total de: ", suma_total(cartasJugador))

cartasCasa= inicioJuego()
print("Cartas de la casa ", cartasCasa[1:3], "[CARTA OCULTA]")
(suma_total(cartasCasa))

if mazoJugador == 21:
    print("HAZ GANADO")

while suma_total(cartasJugador) < 21:
    pregunta= int(input("Desea plantarse (1)\nDesea otra carta(2)"))
    if pregunta == 2:
        add_carta= sample(mazo,1)[0]
        cartasJugador.append (add_carta)
        mazo.remove(add_carta)
        print ("Tus cartas son: ", cartasJugador, "para un total de: ", suma_total(cartasJugador))
    elif pregunta == 1:
        break

if suma_total(cartasJugador)> 21:
    print("Tus cartas suman:", suma_total(cartasJugador), " por lo tanto has pasado de 21\n !HAZ PERDIDO¡")

cartasCasa=juego_casa(cartasCasa)

if suma_total(cartasCasa)>suma_total(cartasJugador): 
    print("El valor total de tus cartas es: ", suma_total(cartasJugador), " mientras que el valor total de las cartas de casa es: ", suma_total(cartasCasa))
    print("Por lo tanto !HAZ GANADO¡")
elif suma_total(cartasCasa)<suma_total(cartasJugador): 
    print("El valor total de tus cartas es: ", suma_total(cartasJugador), " mientras que el valor total de las cartas de casa es: ", suma_total(cartasCasa))
    print("Por lo tanto !HAZ GANADO¡")
elif suma_total(cartasCasa)== suma_total(cartasJugador): 
    print("El valor total de tus cartas es: ", suma_total(cartasJugador), " mientras que el valor total de las cartas de casa es: ", suma_total(cartasCasa))
    print("Por lo tanto !ES UN EMPATE¡")
elif suma_total(cartasCasa)<suma_total(cartasJugador) and suma_total(cartasJugador)>21:
    print("El valor total de tus cartas es: ", suma_total(cartasJugador), " mientras que el valor total de las cartas de casa es: ", suma_total(cartasCasa))
    print("Por lo tanto !HAZ PERDIDO Y LA CASA GANA¡")
elif suma_total(cartasCasa)== suma_total(cartasJugador) and suma_total(cartasJugador)>21 and suma_total(cartasCasa)>21:
    print("El valor total de tus cartas es: ", suma_total(cartasJugador), " mientras que el valor total de las cartas de casa es: ", suma_total(cartasCasa))
    print("Por lo tanto !ES UN EMPATE PERO LOS DOS HAN SUPERADO EL VALOR LIMITE¡")
else:
    print("El valor total de tus cartas es: ", suma_total(cartasJugador), " mientras que el valor total de las cartas de casa es: ", suma_total(cartasCasa))
    print("Por lo tanto !HAZ PERDIDO Y LA CASA GANA¡")