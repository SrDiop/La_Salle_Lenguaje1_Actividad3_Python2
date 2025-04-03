# 📌 Sistema de Gestión de Tareas en Python

Este es un programa en Python que permite gestionar tareas, agregarlas, eliminarlas, marcarlas como completadas y ver su estado.

## 🚀 Funcionalidades

- 📝 **Agregar Tarea**: Permite agregar una nueva tarea con título y descripción.
- ❌ **Eliminar Tarea**: Elimina una tarea seleccionada por el usuario.
- 📋 **Ver Tareas**: Muestra todas las tareas registradas.
- ✅ **Marcar Tarea como Completada**: Cambia el estado de una tarea a "Completada".
- 🔚 **Salir**: Termina la ejecución del programa.

## 🦾 Integrantes del Proyecto

- **Diego Rojas Gonzalez** 

## Estructura
- EJERCICIO 1
    - main.py **Archivo Principal con el menú**
    - funciones.py **Funciones del programa** 
    - README.md **Documentacipon del proyecto**

## Ejecuion
- **python main.py**

## Video Sustentación
- **python main.py**

## Explicacion Codigo

- main.py **Tenemos la navegacion sobre el menú principal y determina cual opcion se ejecutara junto con su funcion**

### Seimportan las funciones de la ruta funciones.py
```python
import funciones
```

### Se inicia con una funcion menu() e imprime las opciones que se van a asignar.
```python
def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
```
![Menú principal](Resources/Images_Readme/Menú.JPG)

### segun la informacion que ingresa el usuario vamos a enviarlo por el if-elif-else a cada una de las funciones establecidas
```python
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
```
### Funciones
-**Agregar Tareas**
```python
def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    tarea = {"titulo": titulo, "descripcion": descripcion, "estado": "Pendiente"}
    tareas.append(tarea)
    print("Tarea agregada correctamente.\n")
```

-**Ver Tareas**
```python
def ver_tareas():
    if not tareas:
        print("No hay tareas registradas.\n")
        return
    print("\nLista de Tareas:")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea['titulo']} - {tarea['descripcion']} [{tarea['estado']}]")
    print("")
```

-**Marcar Tareas Como Completadas**
```python
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
```

-**Eliminar Tareas**
```python
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
```