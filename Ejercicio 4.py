# Escribir un programa que cree un diccionario vacío
# y lo vaya llenado con información sobre una persona
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
# que se le pida al usuario. Cada vez que se añada un
# nuevo dato debe imprimirse el contenido del diccionario.
diccionario = {}

clave = input("Introduzca palabra clave:\n")
while clave != diccionario:
    valor = input("Introduzca el valor:\n")
    diccionario[clave] = valor
    print(diccionario)
    clave = input("Introduzca palabra clave:\n")

