from random import sample

pintas = ["picas", "treboles", "diamantes", "corazones"]
valores = ["A", "J", "Q", "K" ] + [str(i) for i in range (2,11)]
mazo = [(v,p) for v in valores for p in pintas]

def inicioJuego():
    mazoJugador = sample(mazo,2)
    print(mazoJugador)
    for carta in mazoJugador :
        mazo.remove(carta)
        
        
    return mazoJugador
cartasJugador= inicioJuego()
print("Tus cartas ", cartasJugador)
cartasCasa= inicioJuego()
print("Cartas de la casa ", cartasCasa)