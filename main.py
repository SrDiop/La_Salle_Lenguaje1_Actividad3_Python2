import funciones  # Importar las funciones desde funciones.py

#Menú principal del programa
def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar gasto")
        print("2. Eliminar gasto")
        print("3. Ver gastos")
        print("4. Ver gastos * categoria")
        print("5. Calcular total gastos")
        print("6. Salir")
        
#Opcion ingresada por el Usuario        
        opcion = input("Seleccione una opción: ")

#Condicional if-elif-else para determinar que funcion usar   
        if opcion == "1":
            funciones.agregar_gasto()
        elif opcion == "2":
            funciones.eliminar_gasto()    
        elif opcion == "3":
            funciones.ver_gastos()
        elif opcion == "4":
            funciones.ver_resumen_categoria()
        elif opcion == "5":
            funciones.calcular_total_gastos()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.\n")

# Ejecutar el menú nuevamente
menu()
