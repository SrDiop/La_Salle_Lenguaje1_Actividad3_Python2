# Lista para almacenar las tareas
tareas = []

#Función para agregar una nueva tarea
def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    tarea = {"titulo": titulo, "descripcion": descripcion, "estado": "Pendiente"}
    tareas.append(tarea)
    print("Tarea agregada correctamente.\n")

#Función para mostrar todas las tareas
def ver_tareas():
    if not tareas:
        print("No hay tareas registradas.\n")
        return
    print("\nLista de Tareas:")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea['titulo']} - {tarea['descripcion']} [{tarea['estado']}]")
    print("")

#Función para marcar una tarea como completada
def marcar_completada():
    ver_tareas()
    if not tareas:
        return
    try:
        num = int(input("Ingrese el número de la tarea a marcar como completada: "))
        if 1 <= num <= len(tareas):
            tareas[num - 1]["estado"] = "Completada"
            print("Tarea marcada como completada.\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Por favor, ingrese un número válido.\n")

#Función para eliminar una tarea
def eliminar_tarea():
    ver_tareas()
    if not tareas:
        return
    try:
        num = int(input("Ingrese el número de la tarea a eliminar: "))
        if 1 <= num <= len(tareas):
            tarea_eliminada = tareas.pop(num - 1)
            print(f"Tarea '{tarea_eliminada['titulo']}' eliminada.\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Por favor, ingrese un número válido.\n")
