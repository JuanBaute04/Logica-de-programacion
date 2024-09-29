""""
Cadenas

"""

# Cadena simple

cadena =  "Hola, soy  una cadena"
print(cadena)


# Con comillas dobles

cadena = "Esto es una comilla doble\" "
print(cadena)

# Con salto de linea

cadena = "Primer  linea\nSegunda linea"
print(cadena)


#Con caracter asociado
print ("\110\110")

#Raw string

print(r"\110\110")

#Formateo de cadenas

x = 5
cadena = "El numero es:" + str(x)  #Funciona con cualquier operacion matematica
print(cadena)

x = 5
cadena = "El numero es: %d" % x # Para otra cadena se una %s y para un float %f

print(cadena)

# F-strings
x = 5
y = 4
print(f"Los numeros son  {x} y {y}")
print(f"La suma de los numeros es {x + y}") #Funciona con cualquier operacion matematica

#String

cadena_1 = "Hola"
cadena_2 = "como estas?"
print(cadena_1+","+cadena_2)
print(cadena_1*5)

#Pertenencia

print("Hola" in "Hola python") #Devuelve false o true

#Len cuenta los caracteres de mi cadena

print(len("Esta es mi cadena"))

#Buscando dentro de una cadena
cadena = "abcde"
print(cadena[0])
print(cadena[0:2])

#Capitalize (Hace masyuscula la primera letra)

cadena = "hola"
print(cadena.capitalize())


#Lower vuelve las mayusculas minisculas

cadena = "HOLAA"
print(cadena.lower())

#Swapcase vuelve las mayusculas en minusculas y las minusculas en mayusculas

cadena = "HolaAAa"
print(cadena.swapcase())

#Upper convierte todo en mayusculas

cadena = "hola"
print(cadena.upper())

# Count cuenta el numero de coincidencias en una cadena

cadena = 'Bello cuello'
print(cadena.count("llo"))

#Isalnum() devuelve true si la cadena esta formada unicamente por numero y isalpha() devuelve true si esta formada por caracteres alfabeticos

#Strip elimina los caracteres que se le introduce, si no borra los espacios vacios

cadena = " Hola como estas "
print(cadena.strip())

#zfill rellena con ceros a la izquierda

#Join devulve la cadena unida a unos de los elementos de la lista
cadena = "y"
print(cadena.join(["1 ", " 2 ", " 3 "]))

#Split divide las cadenas y las devuelve en una lista

cadena = "Juan,Baute,19"
print(cadena.split())

#Remplazo
print(cadena_1.replace("o", "a "))


#Busqueda de posicion

print("Juan carlos".find("carlos"))



"""
EXTRA

"""

def check(word1,word2:str):
     
     #Palindromos
    print(f"{word1} es un palindromo?:{word1 == word1 [::-1] } ")
    print(f"{word2} es un palindromo?:{word2 == word2 [::-1] } ")
    
    #Anagramas
    print(f"{word1} es un anagrama de {word2}?:{sorted(word1) == sorted(word2)} ")
    
    #Isograma
    print(f"{word1} es un isograma? : :{len(word1)==len(set(word1))} ")
    print(f"{word2} es un isograma? : :{len(word2)==len(set(word2))} ")
    
    def isogram(word:str) -> bool:
     word_dict = dict()
     for word in word2:
        word_dict[word] = word_dict.get(word,0) + 1
        
     isogram = True 
     values = list(word_dict.values())
     isogram_len = values[0]
     for word_count in values:
        if word_count != isogram_len:
          isogram = False
          break
      
     return isogram
    print(f"{word1} es un isograma? :{isogram(word1)} ")
    print(f"{word2} es un isograma? :{isogram(word2)} ")
   
        
check("radar", "python")   
#check("amor","roma")

