import queue

class Proceso:
    def __init__(self, id, nombre, duracion):
        self.id = id
        self.nombre = nombre
        self.duracion = duracion

    def __str__(self):
        return f"Proceso {self.id}: {self.nombre} ({self.duracion}ms)"

class ColaEjecucion:
    def __init__(self):
        self.cola = queue.Queue()

    def agregar_proceso(self, proceso):
        self.cola.put(proceso)

    def obtener_siguiente_proceso(self):
        return self.cola.get() if not self.cola.empty() else None

    def mostrar_pendientes(self):
        return list(self.cola.queue)