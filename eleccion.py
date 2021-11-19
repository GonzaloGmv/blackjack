def elegir(ANTERIOR):
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