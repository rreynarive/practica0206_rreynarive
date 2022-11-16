# Escribir un programa que cree un diccionario de
# traducción español-inglés. El usuario introducirá las
# palabras en español e inglés separadas por dos puntos,
# y cada par <palabra>:<traducción> separados por comas,
# hasta que el usuario introduzca la palabra “terminar”.
# El programa debe crear un diccionario con las palabras
# y sus traducciones. Después pedirá una frase en español y
# utilizará el diccionario para traducirla palabra a palabra.
# Si una palabra no está en el diccionario debe dejarla sin traducir.
diccionario = {}
trad = input("Introduzca la palabra en español y su "
             "traduccion <palabra>:<traduccion>\n")
while trad != "terminar":
   trad.split(":")
   cast = trad[:trad.find(":")]
   ing = trad[trad.find(":")+1:]
   diccionario[cast] = ing
   trad = input("Introduzca la palabra en español y su "
                "traduccion <palabra>:<traduccion>\n")

frase = input("Introduzca una frase para traducirlo:\n")
frase_sep = frase.split(" ")

for palabra in frase_sep :
   if palabra in diccionario.keys():
      print(diccionario[palabra], end=" ")
   else:
      print(palabra, end=" ")

