def my_agenda():
    agenda = {}
    
    def insert_contact(): 
      phone = input("Introduzca el nombre del contacto que desea agendar:")
      if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
          agenda[name]= phone
      else:
          print("El numero debe contener al menos 12 digitos")

    
    while True:
     print("")
     print("1.Buscar contacto")
     print("2.Insertar nuevo contacto")
     print("3.Actualizar contacto")
     print("4.Eliminar contacto")
     print("5.Salir")
     
     option = input("\nSelecione una opcion: ")
     
     match option:
         case "1":
             name = input("Introduzca el nombre del contacto que desea buscar: ")
             if name in agenda:
                 print(f"El contacto {name} posee el siguiente numero telefonico: {agenda[name]}.")
             else:
                 print("El contacto{name} no existe.")
         case "2":
             name = input("Introduzca el nombre del contacto que desea agregar: ")
             insert_contact()
         case "3":
             name = input("Introduzca el nombre del contacto que desea actualizar")
             if name in agenda:
              insert_contact()
              
             else:
                 print("El contacto {name} no existe.")
         case "4": 
             name = input("Introduzca el nombre del contacto que desea eliminar:")
             if name in agenda:
                 del agenda[name]
             else:
                 print("El contacto  {name} no existe.")
         case "5":
             print("El programa finalizo")
             break
         case _:
             print("Opcion invalida,  por favor seleccione una opcion del 1 al 5")

my_agenda()
             
                 
                    
                 
                 
                 
         


    
            