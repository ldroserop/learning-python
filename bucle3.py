'''Bucle que genere una N cantidad de Números Aleatorios solicitada por el usuario
    - Total ingresados
    - Cuantos # son pares
    - Cuantos # son impares
    - Cuantos # son positivos
    - Cuantos # son negativos
    - Suma de # positivos
    - Suma de # egativos
'''
import os
import random

os.system('clear')

def numbers_generator(cant):
    i = 1
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    sum_pos = 0
    sum_neg = 0
    while i <= cant:
        num = random.randint(-10, 10)
        print(num)
        

        if num % 2 == 0:
            pares = pares + 1
        else:
            impares += 1

        if num > 0:
            positivos = positivos + 1
            sum_pos = sum_pos + num
        else:
            negativos += 1
            sum_neg += num

        i += 1
    print(f"Total de números generados: {cant}")
    print(f"Total de números pares: {pares}")
    print(f"Total de números impares: {impares}")
    print(f"Total de números positivos: {positivos}")
    print(f"Total de números negativos: {negativos}")
    print(f"Suma de números positivos: {sum_pos}")
    print(f"Suma de números negativos: {sum_neg}")


cant_num = int(input("¿Qué cantidad de números deseas generar?: "))
numbers_generator(cant_num)
