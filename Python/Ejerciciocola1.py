from colorama import init, Fore, Style
import colaclinica

# Inicializa colorama
init(autoreset=True)

def mostrar_menu():
    """
    Muestra el menú principal de opciones para el usuario.
    """
    print(Fore.CYAN + "=== Clínica - Sistema de Atención ===")
    print(Fore.GREEN + "1. Agregar paciente")
    print(Fore.YELLOW + "2. Atender paciente")
    print(Fore.BLUE + "3. Mostrar cola de pacientes")  
    print(Fore.RED + "4. Salir")
    print(Style.RESET_ALL)

# Bucle principal del programa: se ejecuta hasta que el usuario decida salir.
while True:
    mostrar_menu()
    opcion = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)

    # Opción 1: Agregar un nuevo paciente a la cola
    if opcion == "1":
        nombre = input(Fore.GREEN + "Ingrese el nombre del paciente: " + Style.RESET_ALL)
        colaclinica.agregar_paciente(nombre)

    # Opción 2: Atender al primer paciente en la cola
    elif opcion == "2":
        colaclinica.atender_paciente()

    # Opción 3: Mostrar la lista actual de pacientes en espera
    elif opcion == "3":
        colaclinica.mostrar_cola()

    # Opción 4: Salir del sistema
    elif opcion == "4":
        print(Fore.RED + "Saliendo del sistema. ¡Gracias!" + Style.RESET_ALL)
        break

    # Cualquier otra opción se considera inválida
    else:
        print(Fore.RED + "Opción inválida. Intente de nuevo.\n" + Style.RESET_ALL)
