from random import shuffle

cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
} 
print("Estas son las cartas y sus valores: ", cartas)
claves_cartas = list(cartas.keys())
barajar = list(cartas.keys())
valores_cartas = list(cartas.values())
shuffle(barajar)

while True:
    carta1 = input("Elija una carta sin mirarla: ")
    try:
        carta1 = int(carta1)
    except:
        pass
    else:
        if 0 <= carta1 <= 12:
            break
while True:
    carta2 = input("Elija una segunda carta sin mirarla: ")
    try:
        carta2 = int(carta2)
    except:
        pass
    else:
        if carta2 != carta1 and 0 <= carta2 <= 12:
            break
print("Estas son sus cartas: ", barajar[carta1], barajar[carta2])

indice1 = claves_cartas.index(barajar[carta1])
indice2 = claves_cartas.index(barajar[carta2])
valor1 = valores_cartas[indice1]
valor2 = valores_cartas[indice2]
valorT = valor1 + valor2
print("Este es el valor de sus cartas: ", valorT)