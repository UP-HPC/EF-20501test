import multiprocessing  # Importamos multiprocessing para trabajar con procesos
import time  # Para simular una tarea pesada
import math  # Para cálculos matemáticos

def calcular_factorial(n):
    """Calcula el factorial de un número"""
    print(f"Calculando factorial de {n}...")
    time.sleep(2)  # Simula un proceso pesado
    print(f"Resultado factorial: {math.factorial(n)}")

def calcular_suma(lista):
    """Calcula la suma de una lista de números"""
    print(f"Calculando suma de {lista}...")
    time.sleep(2)  # Simula un proceso pesado
    print(f"Resultado suma: {sum(lista)}")

if __name__ == "__main__":
    num = 5  # Número para el factorial
    lista = [1, 2, 3, 4, 5]  # Lista de números a sumar

    # Creamos dos procesos, uno para cada tarea
    proceso1 = multiprocessing.Process(target=calcular_factorial, args=(num,))
    proceso2 = multiprocessing.Process(target=calcular_suma, args=(lista,))

    # Iniciamos los procesos
    proceso1.start()
    proceso2.start()

    # Esperamos a que ambos procesos terminen antes de continuar
    proceso1.join()
    proceso2.join()

    print("Tareas completadas")  # Mensaje final indicando que todo terminó
