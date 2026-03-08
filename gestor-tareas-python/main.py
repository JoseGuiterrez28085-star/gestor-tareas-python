tareas = []

while True:
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. salir")
    
    opcion = input ("Elige una opcion: ")
    
    if opcion == "1":
        if len(tareas) == 0:
            print ("No hay tareas.")
        else:
            for i, tarea in enumerate(tareas):
                        print(f"{i+1}.{tareas} ")
    elif opcion == "2":
         nueva = input("Escrie la nueva tarea: ")
         tareas.append(nueva)
         print("Tarea agregada.")
    
    elif opcion == "3":
        num = int(input("Numero de tareas a eliminar: "))
        if 0 <num <= len(tareas):
            tareas.pop(num-1)
            print("Tarea eliminada.")
        else:
            print("Numero invalido.")
            
    elif opcion == "4":
        print("Hasta luego!")
        break
    else:
        print("Opcion no valida.")                                              