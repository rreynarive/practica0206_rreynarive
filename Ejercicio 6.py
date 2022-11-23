clase = [{"73464267j": {"nombre": "Rosa", "apellido": "Reyna", "telefono": "123456789", "correo": "reynarive@educacion.es", "aprobado": True}},
         {"12345678m": {"nombre": "Jos", "apellido": "Aba", "telefono": "125478964", "correo": "abajos@educacion.es", "aprobado": False}}]
for i in clase:
    print(i)

opci = "Eliga la siguente accion:\n"\
       "(1)- Añadir un alumno/a\n"\
       "(2)- Eliminar un alumno/a\n"\
       "(3)- Mostrar datos de un alumno/a\n"\
       "(4)- Listar todo el alumnado\n"\
       "(5)- Listar alumnados aprobados\n"\
       "(6)- Terminar\n"

menu = input(opci)
while menu != "6":
    if menu == "1":
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


    if menu == "2":
        NIF = input("Introduce el NIF del alumno para eliminar:\n")
        alumno = {NIF: " "}
        if NIF in clase:
            clase.remove(alumno)
        else:
            print("No existe el alumno con el NIF", NIF)
        for i in clase:
            print(i)


    if menu == "3":
        NIF = input("Introduce el NIF del alumno para mostrar:\n")
        if NIF in clase:
            clase[0]

    if menu == "4":
        print("Lista de todo el alumnado")


    if menu == "5":
        print("Lista de alumnados aprobados")
