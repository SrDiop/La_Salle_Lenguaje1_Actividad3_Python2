import funciones  # Importar las funciones desde funciones.py

#Menú principal del programa
def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        
#Opcion ingresada por el Usuario        
        opcion = input("Seleccione una opción: ")

#Condicional if-elif-else para determinar que funcion usar   
        if opcion == "1":
            funciones.agregar_tarea()
        elif opcion == "2":
            funciones.ver_tareas()
        elif opcion == "3":
            funciones.marcar_completada()
        elif opcion == "4":
            funciones.eliminar_tarea()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.\n")

# Ejecutar el menú nuevamente
menu()
