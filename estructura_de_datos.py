"""
Estructuras de datos

"""

# Listas

mylist = ["Juan","Baute", "Hola"]

mylist.append("mari") #Agrega a la lista

# mylist.extend("Hola Como estas?") # Tambien agrega a la lisga

mylist[0] = "Juancito" #Actualiza datos de la lista

mylist.remove("mari")  #Elimina un elemento de la lista
print(mylist[1]) 

mylist.sort() #ordena  la lista de menor a mayor


mylist.pop(2)  #Elimina el elemento en la posicion 9 de la lista


# mylist.clear() elimina todos los datos de la lista


print(mylist )

# Tuplas

tupla: tuple = ("Juan","Baute","19")
print(tupla[1]) # Acceso
tupla = tuple [sorted(tupla)] # Ordenacion
print(tupla)


# Sets

my_set = {"Juan","Baute","19"}
print(my_set)
my_set.add("juanbautejb88@gmail.com") # Insercion
print(my_set)
my_set.remove("Baute")
print(my_set)


# Diccionarios  

my_dict =  {"nombre":"Juan","edad":19,"ciudad":"Ocumare"} 

my_dict["email"] = "juanbautejb88@gmail.com" #Insercion
 
my_dict["edad"]  = 20 #Actualizacion

del my_dict["ciudad"]  #Eliminacion

my_dict = dict(sorted(my_dict.items()))  # Ordenacion

print (my_dict["edad"]) #Acceso
print(my_dict)


"""
EXTRA

"""

def my_agenda():
    agenda = {}
    
    def insert_contact():
        phone = input("Inserte el numero telefonico:")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] =phone
        else: 
            print("El numero debe contener al menos 12 digitos")
    while True:  
        print("")
        print("1.Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        
        option = input("\nSeleciona una opcion: ")
        
        match option:
            case "1":
                name = input("Introduce el nombre del contacto que desea buscar: ")
                if name in agenda:
                    print(
                        f"El numero de telefono de {name} es {agenda[name]}"
                    )
                else:
                    print(f"El contacto {name} no existe")
            case  "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")


my_agenda()

