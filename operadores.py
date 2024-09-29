# Operadores aritmeticos

print(f"Suma de 10 + 3 = {10 + 3}")
print(f"Resta de 10 - 3 = {10 - 3}")
print(f"Multiplicacion de 10 * 3 = {10 * 3}")
print(f"Division de 10 / 2 = {10 / 2}")
print(f"Division entera de 10 / 3 = {10 / 3}")
print(f"Potenciacion de 10 ** 3 = {10 ** 3}")
print(f"El residuo de de 10 / 3 = {10 % 3}")


print('------------------')
# Operadores de comparacion 

print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad:10 != 3 es {10 != 3}")
print(f"Menor que: 10 < 11 es {10 < 11}")
print(f"Mayor que: 10 > 5 {10 > 5}")
print(f"Mayor o igual que: 10 >= 10 {10 >= 10}")
print(f"Menor o igual que: 10 <= 10 {10 <= 10}")

print('------------------')
# Operadores logicos

print(f'AND: 10 + 3 == 13 AND 5 - 1 == 4 es {10 + 3 == 13 and  5 - 1 == 4}')
print(f'OR: 10 + 3 == 13 AND 5 - 1 == 3  es {10 + 3 == 13 or  5 - 1 == 3}')
print(f'NOT: 10 + 3 == 13 AND 5 - 1 == 4  es { not 10 + 3 == 13 and  5 - 1 == 4}')


print('------------------')

# Operador de asignacion

my_number = 10 
print(my_number)

my_number += 4 #Suma y asignacion
print(my_number)

my_number -= 4 # Resta y asignacion
print(my_number)

my_number *= 4 # Multiplicacion y asignacion
print(my_number)

my_number /= 2 # Division y asignacion
print(my_number)

my_number //= 4 # Division entera y asignacion
print(my_number)

my_number **= 4 # Potenciacion y asignacion
print(my_number)

my_number %= 3 # Residuo y asignacion
print(my_number)

print('------------------')

# Operadores de identidad
my_new_number = my_number
print(f'my number es my_new_number es {my_number is my_new_number}')
print(f'my number es my_new_number es {my_number is not  my_new_number}')

print('------------------')

# Operadores de pertenencia 

print(f'u in Juan =  { 'u' in "Juan"}')
print(f'h not in Juan =  { 'u' not in "Juan"}')

print('------------------')

# Operadores de bit

a = 10
b = 3

print(f"AND: 10 & 3 = {10 & 3}")
print(f"OR: 10 | 3 = {10 | 3}")
print(f"XOR: 10 ^ 3 = {10 ^ 3}")
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")

print('------------------')
# Estructuras de control

#Condicionales

my_string = "Juancio"

if my_string == "Juancito":
 print('Hola Juancito')
elif my_string == "Baute":
    print("Hola Baute")
    
else:
    print("no se quien eres, puedes indicar tu nombre:")
    
print('------------------') 
# Iterativos 

for i in range(11):
    print(i)
 
i = 0   
while i <= 10:
    print(i)
    i += 1

    
# Manejo de excepciones
print('------------------') 

try: 
 print(10/1)
except:
    print("Se ha producido un error")
finally:
    print("Ha terminado el manejo de excepciones")
    
 
# EXTRA


for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
     print(number)
    



   
 







