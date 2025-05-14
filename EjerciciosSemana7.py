"""
Ejercicio #4: Simulación de atención de procesos por el microprocesador
Diseñe un programa que simule cómo un microprocesador atiende procesos en una cola de ejecución.
ejecución. Cada proceso tiene un identificador, un nombre y una duración estimada 
en milisegundos. A medida que el procesador queda libre, atiende al siguiente 
proceso en orden de llegada (FIFO - First In, First Out). El sistema debe 
permitir agregar procesos a la cola, mostrar el proceso en ejecución y visualizar 
los procesos pendientes.
"""
import time
from ModulosSemana7 import Proceso, ColaEjecucion

def ejecutar_procesador(cola):
    while not cola.cola.empty():
        proceso = cola.obtener_siguiente_proceso()
        if proceso:
            print(f"Ejecutando: {proceso}")
            time.sleep(proceso.duracion / 1000)  # Simulación de duración
        else:
            print("No hay procesos pendientes.")

def main():
    cola = ColaEjecucion()

    cola.agregar_proceso(Proceso(1, "Compilar código", 2000))
    cola.agregar_proceso(Proceso(2, "Cargar recursos", 1500))
    cola.agregar_proceso(Proceso(3, "Renderizar imagen", 3000))

    print("\nProcesos pendientes:")
    for p in cola.mostrar_pendientes():
        print(p)

    print("\nIniciando ejecución...\n")
    ejecutar_procesador(cola)

if __name__ == "__main__":
    main()
