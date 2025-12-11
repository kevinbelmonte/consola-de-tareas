tareas = []

while True:
    print("\n=== LISTA DE TAREAS ===")
    print("1. agregar tarea")
    print("2. ver tareas")
    print("3. salir")

    opcion = input("elegir una opción: ")

    if opcion == "1":
        tarea = input("nueva tarea: ")
        tareas.append(tarea)
        print("tarea agregada.")
    elif opcion == "2":
        print("\ntus tareas:")
        for t in tareas:
            print("-", t)
    elif opcion == "3":
        print("hasta pronto")
        break
    else:
        print("opción inválida.")
