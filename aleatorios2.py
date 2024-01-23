'''Script que genere el lanzamiento de 2 dados (1-6) 
y que muestre en pantalla el mensaje ganador cuando genere pares iguales,
de lo contrario, el mensaje dirá: sigue intentando'''

#Importar biblioteca para generar números aleatorios enteros
from random import randint

#Generar y lanzar los valores de los dados
def dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)

    return dice1, dice2

#Salidas
d = dices()
d1 = d[0]
d2 = d[1]

print("Dados: ", d)
print("Dice 1: ", d1)
print("Dice 2: ", d2)
