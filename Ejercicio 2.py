# Escribir un programa que pregunte al usuario
# su nombre, edad, dirección y teléfono y lo guarde
# en un diccionario. Después debe mostrar por pantalla
# el mensaje “<nombre> tiene <edad> años, vive en <dirección>
# y su número de teléfono es <teléfono>”.
nombre = input("Introduzca su nombre:\n")
edad = input("Introduzca su edad:\n")
direccion = input("Introduzca su direccion:\n")
telefono = input("Introduzca su telefono:\n")
nombre = nombre.title()
direccion = direccion.title()
datos = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}

print((datos["nombre"] + (" tiene ") +
       (datos["edad"]) + (" años, vive en ") +
       (datos["direccion"]) + (" y su numero de telefono es ") +
       (datos["telefono"])))