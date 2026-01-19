from contacto import Contacto
from gestorcontactos import GestorContactos

# Interfaz de usuario

def menu():
    agenda = GestorContactos()

    while True:
        print("\n----Sistema de Gestión de Contactos----")
        print("1. Agregar Contacto")
        print("2. Editar Contacto")
        print("3. Eliminar Contacto")
        print("4. Buscar Contacto por Nombre")
        print("5. Buscar Contacto por Teléfono")
        print("6. Mostrar Contactos")
        print("7. Salir")

        opcion = (input("Seleccione una opción: ")).strip()
        print("\n")
        
        if opcion == "1":
            nombre = input("Nombre: ").strip()
            telefono = input("Teléfono: ").strip()
            email = input("Email: ").strip()
            direccion = input("Dirección: ").strip()
            try:
                nuevo_contacto = Contacto(nombre, telefono, email, direccion)
                if agenda.agregar_contacto(nuevo_contacto):
                    print("✔️ Contacto agregado correctamente.")
                else:
                    print("⚠️ Ya existe un contacto con ese teléfono.")
            except ValueError as e:
                print(str(e))
                               
        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto a editar: ").strip()
            resultados = agenda.buscar_por_nombre(nombre)

            if not resultados:
                print(f"\n⚠️ No se encontró el contacto {nombre} en la Agenda.")
            else: 
                contacto = resultados[0]
                # Mostrar datos actuales antes de pedir cambios 
                print("\nDatos actuales del contacto:") 
                print(contacto)

                # Pedir nuevos datos (Enter mantiene el valor actual)
                nuevo_nombre = input("Nuevo nombre (Enter para mantener actual): ") or None 
                nuevo_telefono = input("Nuevo teléfono (Enter para mantener actual): ") or None
                nuevo_email = input("Nuevo email (Enter para mantener actual): ") or None
                nueva_direccion = input("Nueva dirección (Enter para mantener actual): ") or None

                try:
                    if agenda.editar_contacto(nombre, nuevo_nombre, nuevo_telefono, nuevo_email, nueva_direccion):
                        print("✔️ Contacto editado correctamente.")
                    else:
                        print("⚠️ Ocurrió un problema al editar el contacto.")
                except ValueError as e:
                    print(str(e))
            
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
            if agenda.eliminar_contacto(nombre):
                print(f"\nContacto {nombre} eliminado.")
            else:
                print("\n⚠️ Contacto no encontrado en la Agenda.")
            
        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ").strip()
            resultados = agenda.buscar_por_nombre(nombre)
            if resultados:
                print("\n".join(str(c) for c in resultados))
            else:
                print("\n⚠️ No se encontraron contactos con ese nombre.")

        elif opcion == "5":
            telefono = input("Ingrese el número de teléfono a buscar: ").strip()
            resultados = agenda.buscar_por_telefono(telefono)
            if resultados:
                print("\n".join(str(c) for c in resultados))
            else:
                print("\n⚠️ No se encontraron contactos con ese teléfono.")

        elif opcion == "6"  :
            contactos = agenda.mostrar_contactos()
            if contactos :
                print("Nombre               | Teléfono     | Email                     | Dirección")
                print("-"*80) 
                for c in agenda.contactos: print(c)
            else:
                print("⚠️ No hay contactos registrados en la Agenda.")

        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta pronto!. ")
            break

        else:
            print("❌ Opción inválida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()