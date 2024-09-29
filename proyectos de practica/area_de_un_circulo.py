import math

radio = float(input("Ingresa el radio del circulo que desea calcular:"))

area =  math.pi * 100 * radio ** 2 // 100 #La multiplicacion y division por 100 es para obtener un numero redondo.

print(f"El area del circulo con radio {radio} es {area}")

