from random import shuffle
import random
#Diccionario
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

#Paso el diccionario a listas
claves_cartas = list(cartas.keys())
valores_cartas = list(cartas.values())
barajar = claves_cartas * 4
shuffle(barajar)

#Eleccion de cartas
while True:
    NcartaJ1 = input("Elija una carta sin mirarla: ")
    try:
        NcartaJ1 = int(NcartaJ1)
    except:
        pass
    else:
        if 0 <= NcartaJ1 <= 51:
            break
while True:
    NcartaJ2 = input("Elija una segunda carta sin mirarla: ")
    try:
        NcartaJ2 = int(NcartaJ2)
    except:
        pass
    else:
        if 0 <= NcartaJ2 <= 51:
            break
cartaJ1 = barajar[NcartaJ1]
cartaJ2 = barajar[NcartaJ2]
print("Estas son sus cartas: ", cartaJ1, cartaJ2)

#Calculo el indice comparando elementos y pasando ese indice a la lista de valores
indiceJ1 = claves_cartas.index(cartaJ1)
indiceJ2 = claves_cartas.index(cartaJ2)
#Calculo el valor comparando indices
valorJ1 = valores_cartas[indiceJ1]
valorJ2 = valores_cartas[indiceJ2]
valorJT = valorJ1 + valorJ2
print("Este es el valor de sus cartas: ", valorJT)
