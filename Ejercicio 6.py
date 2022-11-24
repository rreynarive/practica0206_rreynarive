
clase = [{"73464267j": {"nombre": "Rosa", "apellido": "Reyna", "telefono": "123456789", "correo": "reynarive@educacion.es", "aprobado": True}},
          {"12345678j": {"nombre": "Lucas", "apellido": "Rodriguez", "telefono": "636345098", "correo": "rodrilu@educacion.es", "aprobado": False}}]

for i in clase:
    print(i)

while True:

    print("(1)- Añadir un alumno/a")
    print("(2)- Eliminar un alumno/a")
    print("(3)- Mostrar datos de un alumno/a")
    print("(4)- Listar todo el alumnado")
    print("(5)- Listar alumnados aprobados")
    print("(6)- Terminar")
    menu = int(input("Elija un de las siguientes acciones:"))

    if menu == 1:
        NIF = input("Introduce el NIF del alumno:\n")
        nombre = input("Introduce el nombre del alumno:\n")
        apellido = input("Introduce el apellido del alumno:\n")
        telefono = input("Introduce el telefono del alumno:\n")
        correo = input("Introduce el correo del alumno:\n")
        aprobado = input("¿El alumno ha aprobado?(True/False)\n")
        datos = {"nombre": nombre, "apellido": apellido, "telefono": telefono, "correo": correo, "aprobado": aprobado}
        alumno = {NIF: datos}
        clase.append(alumno)
        for i in clase:
            print(i)


    elif menu == 2:
        NIF = input("Introduce el NIF del alumno para eliminar:\n")
        e = clase[:clase.find(":")]
        for e in clase:
            if e == ["NIF"]:
                NIF: clase.remove(e)




    elif menu == 3:
        NIF = input("Introduce el NIF del alumno para mostrar:\n")
        print(len(clase))



    elif menu == 4:
        print("Lista de todo el alumnado")



    elif menu == 5:
        print("Lista de alumnados aprobados")



    if menu == 6:
        break
