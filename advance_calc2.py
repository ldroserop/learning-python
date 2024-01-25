import os

os.system("clear")

def calculator(x, y, z):
    if z == '1' :
        return x + y
    elif z == '2' :
        return x - y
    elif z == '3' :
        return x * y
    elif z == '4' :
        if y == 0:
            return 'No se puede dividir entre cero (0)'
        return x / y
    elif z == '5':
        '''suma = x + y
        resta = x - y
        multiplicacion = x * y
        if y == 0:
            division = 'No se puede dividir entre cero (0)'
        else:
            division = x / y
        return {
            'Suma': suma,
            'Resta': resta,
            'Multiplicación': multiplicacion,
            'División': division
        }'''
    else :
        print ("::: Opción Inválida :::")
        return 0

n1 = float(input("Ingrese el primer valor: "))
n2 = float(input("Ingrese el segundo valor: "))

print("::: Menú Calculadora :::")
print("[1.] Sumar")
print("[2.] Restar")
print("[3.] Multiplicar")
print("[4.] Dividir")
print("[5.] Todas")

opc = input("Digite una opción del menú: ")

ans = calculator(n1, n2, opc)

print("Resultado: ", ans)