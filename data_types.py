#Tipo de datos en Python
#Python es un lenguaje dinámicamente tipado --> No es necesario declarar el tipo de dato

#1. Numéricos
##Enteros Z => int
num1 = 42
print("Num1: ", type(num1))
##Flotantes o decimales => float
num2 = 50.5
print("Num2: ", type(num2))
##Complejos => complex
num3 = 2j
print("Num3: ", type(num3))

#2. Cadena
my_name = "Luis"
print("my_name", type(my_name))
my_lastname = "Rosero"
print("my_lastname", type(my_lastname))
profile = '''
    Luis es una persona enfocada
    en sus estudios'''
print("profile", type(profile))
address = 'Calle 18A #42-76'
print("address", type(address))

a = 1
b = 1
suma1 = a + b

c= "1"
d= '1'
suma2 = c + d

print("Suma1: ",suma1)
print("Suma2: ",suma2)

#3. Lógicos (booleanos => True o False)
usuario_activo = True
print("Usuario Activo: ", type(usuario_activo))
pago_realizado = False
print("Pago Realizado: ", type(pago_realizado))

#4. Listas
detodito = ['Luis', 25, 20000, 'Calle 18A #42-76', 1.70, 72]
frutas = ['Manzana', 'Banano']
colors = ['Azúl', 'Rojo', 'Blanco']
print("Detodito: ", detodito, type(detodito[1]))
print("Frutas: ", frutas, type(frutas))
print("Colores: ", colors, type(colors))

#5. Tuplas
#6. Diccionarios
#7. Conjuntos