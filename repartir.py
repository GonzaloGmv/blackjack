import random
def jugador(ANTERIOR):
    while True:
        elegida = input("Elija una carta sin mirarla: ")
        try:
            elegida = int(elegida)
        except:
            pass
        else:
            if elegida != ANTERIOR and 0 <= elegida <= 51:
                break
    return elegida

def banca(NCARTAJ1, NCARTAJ2, ANTERIOR):
    while True:
        carta_banca = random.randrange(0, 51)
        if carta_banca != NCARTAJ1 and carta_banca != NCARTAJ2 and carta_banca != ANTERIOR:
            break
    return carta_banca