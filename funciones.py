# Lista para almacenar las tareas
gastos = []

#Función para agregar un gasto
def agregar_gasto():
    categoria = input("Ingrese la categoria del gasto: ")
    descripcion = input("Ingrese la descripción del gasto: ")
    monto = float(input("Ingrese la descripción del gasto: "))
    gasto = {"categoria": categoria, "descripcion": descripcion, "monto": monto}
    gastos.append(gasto)
    print("gasto agregado correctamente.\n")

#Función para mostrar todos los gastos
def ver_gastos():
    if not gastos:
        print("No hay gastos registrados.\n")
        return
    print("\nLista de Gastos:")
    for i, gasto in enumerate(gastos, 1):
        print(f"{i}. {gasto['categoria']} - {gasto['descripcion']} [{gasto['monto']}]")
    print("")

#Función para mostrar un resumen de gastos por categoria
#def ver_resumen_categoria():

#Función para calcular el total de los gastos
#def calcular_total_gastos():

#Función para eliminar una tarea
def eliminar_gasto():
    ver_gastos()
    if not gastos:
        return
    try:
        num = int(input("Ingrese el número del gasto a eliminar: "))
        if 1 <= num <= len(gastos):
            gasto_eliminada = gastos.pop(num - 1)
            print(f"Tarea '{gasto_eliminada['categoria']}' eliminado.\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Por favor, ingrese un número válido.\n")