from random import shuffle
import repartir, ganador

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
#Cada carta y su valor
for carta, valor in cartas.items():
    print("La carta {} vale {}".format(carta, valor))
#Para imprimir esto, he mirado el código que se encontraba en el archivo Guía/23_Diccionario/23__01_Introduccion.py y he copiado esa parte, ya que está más ordenado que como lo había hecho yo

#Paso el diccionario a listas
claves_cartas = list(cartas.keys())
valores_cartas = list(cartas.values())
barajar = claves_cartas * 4
shuffle(barajar)
print("Se barajan las cartas...")

#JUGADOR
#Eleccion de cartas
NcartaJ1 = repartir.jugador("")
print("Ahora escoja otra carta")
NcartaJ2 = repartir.jugador(NcartaJ1)
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

#BANCA
#Seleccion de cartas
NcartaB1 = repartir.banca(NcartaJ1, NcartaJ2, "")
NcartaB2 = repartir.banca(NcartaJ1, NcartaJ2, NcartaB1)
cartaB1 = barajar[NcartaB1]
cartaB2 = barajar[NcartaB2]
print("Estas son las cartas de la banca: ", cartaB1, cartaB2)
#Calculo de valores como con el jugador
indiceB1 = claves_cartas.index(cartaB1)
indiceB2 = claves_cartas.index(cartaB2)
valorB1 = valores_cartas[indiceB1]
valorB2 = valores_cartas[indiceB2]
valorBT = valorB1 + valorB2
print("Este es el valor de las cartas de la banca: ", valorBT)

#Se comparan las cartas para ver quien gana
ganador.comparar(valorJT, valorBT)