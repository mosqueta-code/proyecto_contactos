# Definición de la clase GestorContactos
from contacto import Contacto

class GestorContactos:
    def __init__(self):
        self.contactos = []         # Lista de contactos

    def agregar_contacto(self, contacto):        
        if any(c.get_telefono() == contacto.get_telefono() for c in self.contactos): 
            return False
        self.contactos.append(contacto)
        return True        
        
    def editar_contacto(self, nombre, nuevo_nombre = None, nuevo_telefono = None, nuevo_email = None, nueva_direccion = None):  
        for c in self.contactos:
            if nombre.lower() == c.get_nombre().lower():
                if nuevo_nombre is not None: c.set_nombre(nuevo_nombre)
                if nuevo_telefono is not None: c.set_telefono(nuevo_telefono)
                if nuevo_email is not None: c.set_email(nuevo_email)
                if nueva_direccion is not None: c.set_direccion(nueva_direccion)
                return True
        return False             
       
    def eliminar_contacto(self, nombre):        
        for c in self.contactos:
            if c.get_nombre().lower() == nombre.lower():
                self.contactos.remove(c)
                return True
        return False                                      
        
    def buscar_por_nombre(self, nombre):      
        return [c for c in self.contactos if nombre.lower() == c.get_nombre().lower()]
    
    def buscar_por_telefono(self, telefono):     
        return [c for c in self.contactos if c.get_telefono() == telefono]
    
    def mostrar_contactos(self):      
        return [str(c) for c in self.contactos]
