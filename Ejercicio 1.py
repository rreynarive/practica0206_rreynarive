# Escribir un programa que guarde en una variable
# el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
# pregunte al usuario por una divisa y muestre su símbolo
# o un mensaje de aviso si la divisa no está en el diccionario.
dictionary = {"Euro": "€", "Dollar": "$", "Yen": "¥"}
divisa = input("Introduzca divisa:\n")
divisa = divisa.title()
if divisa in dictionary:
   print(dictionary[divisa])
else:
    print("Esta divisa no esta en el diccionario")