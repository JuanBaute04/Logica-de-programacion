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

