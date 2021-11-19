def comparar(VALORJ, VALORB):
    if VALORJ > 21:
        print("El valor de sus cartas es mayor que 21. Ha perdido")
    elif VALORB > 21:
        print("El valor de las cartas de la banca es mayor que 21. Ha ganado")
    else:
        if VALORJ > VALORB:
            print("El valor de sus cartas esta mas cerca de 21 que el de la banca. Ha ganado")
        elif VALORB > VALORJ:
            print("El valor de las cartas de la banca esta mas cerca del 21 que el suyo. Ha perdido")
        else:
            print("El valor de sus cartas es el mismo que el de las cartas de la banca. Empate")