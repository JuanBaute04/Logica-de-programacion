"""
Funciones definidas por el usuario

"""
# Funcion simple


def saludo():
    print("Hola,python")
    
saludo() 

#  Funcion con retorno

def return_saludo():
    return "!Hola, python!"

print(return_saludo())


# Funcion con argumento


def saludo_nombre(nombre):
    print("Hola", nombre)
saludo_nombre("Juan")

# Funcion con argumentos

def saludo_nombre(saludo,nombre,apellido):
    print(f"{saludo}, {nombre}, {apellido}!")

saludo_nombre(nombre="Juan",saludo="Hola",apellido="Baute")



# Funcion con argumento predeterminado 

def pred_saludo_nombre(nombre="Python"):
    print(f"Hola, {nombre}")
pred_saludo_nombre("Juan")
pred_saludo_nombre()


# Funcion con argumento y retorno

def return_arg_saludo(saludo, nombre):
    return f"{saludo},{nombre}"

print(return_arg_saludo("Hola","Juan"))

# Con retorno de varios valores

def multiple_return_saludo():
    return  "Hola", "Python"

saludo , nombre = multiple_return_saludo()

print(saludo)
print(nombre)

#  Con numero variable de argumentos

def variable_arg_saludo(*names):
    for name  in names:
        print(f"Hola, {name}!!" )
        
variable_arg_saludo("Python","Juan",  "Mari")


# Con numero variable de argumento pero con palabra clave\
    
def variable_key_saludo(**nombres):
    for key , value in nombres.items():
     print (f"{value} ({key})!!")
       
variable_key_saludo(
    lenguaje ="Python",
    nombre="Juan", 
    Novia = "Mari" 
 )

""""
Funciones dentro de funciones

"""

def outer_funtion():
    def inner_funtion():
        print("Funcion interna: Hola,python")
    inner_funtion()     
outer_funtion(  )        



"""
Funciones del lenguaje

"""

print(len("Juancito"))
print(type(256))
print("Juancito".upper())

"""
Variables locales y globales
"""

global_variable = "Python"
print(global_variable)

def hola_python():
    local_variable = "Hola"
    print(f"{local_variable},{global_variable}")
    
hola_python()




# EXTRA

def print_number(text_1,text_2 )-> int:
    count = 0

    for number in range (1,101):  
        if number % 3 == 0 and number  % 5 == 0:
         print(text_1 + text_2)
        if number% 3 == 0:
            print(text_1)
        elif  number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count    

    
        
        
print(print_number("Fizz","Buzz"))       
            


