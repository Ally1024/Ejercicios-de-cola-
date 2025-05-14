""""
Buenos dias profe  somos Allysson Palma, Nicole Ramos y Andres  Porras 
y hoy les traemos un programa que simula una cola de pacientes en una clínica.

Ejercicio:Desarrolle un programa en Python que simule una cola de atención en una clínica. El sistema
debe permitir agregar pacientes a la cola (registro de llegada), atender al siguiente paciente
(eliminar el primero en la cola) y mostrar en pantalla la lista actual de pacientes en espera. El
docente implementará el programa paso a paso, explicando cada parte del código, mientras los
estudiantes proponen mejoras, prueban con distintos datos y analizan el comportamiento de la
estructura tipo cola.
el programa utiliza la biblioteca colorama para mejorar la presentación de la salida en consola.
 colorama ayuda a cambiar el color de los textos y estilos como negrita o subrayado.
Lo que hace que la salida del programa sea más atractiva y fácil de leer. 
init() es necesario para inicializar colorama y hacer que los colores funcionen correctamente, especialmente en Windows.
Fore se usa para cambiar el color del texto. Los colores disponibles incluyen Fore.RED para rojo, Fore.GREEN para verde, Fore.YELLOW para amarillo, etc.
Style se usa para cambiar el estilo del texto. En el código, usamos Style.RESET_ALL para resetear cualquier color o estilo aplicado previamente.
"""
from colorama import init, Fore, Style

# Inicializa colorama 
init(autoreset=True)

# Lista que simula la cola de pacientes en la clínica
cola_pacientes = []

# Agrega un paciente al final de la cola de atención
def agregar_paciente(nombre):
    cola_pacientes.append(nombre)
    print(Fore.GREEN + f"Paciente '{nombre}' ha sido agregado a la cola.\n")

# Atiende al siguiente paciente en la cola (el primero que llegó)
def atender_paciente():
    if cola_pacientes:
        paciente = cola_pacientes.pop(0)
        print(Fore.BLUE + f"Paciente '{paciente}' ha sido atendido.\n")
    else:
        print(Fore.RED + "No hay pacientes en espera.\n")

# Muestra en pantalla la lista actual de pacientes en espera
def mostrar_cola():
    if cola_pacientes:
        print(Fore.YELLOW + "Pacientes en espera:")
        for i, paciente in enumerate(cola_pacientes, start=1):
            print(f"{i}. {paciente}")
        print()
    else:
        print(Fore.WHITE + "No hay pacientes en espera.\n")
