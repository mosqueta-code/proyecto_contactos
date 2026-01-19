# Definición de la clase Contacto 
import re

class Contacto:
    def __init__(self, nombre, telefono, email, direccion):
        if not self.validar_nombre(nombre):
            raise ValueError("❌ El nombre no puede estar vacío.")
        if not self.validar_telefono(telefono):
            raise ValueError("❌ Teléfono inválido. Debe contener solo dígitos y tener al menos 7 caracteres.")
        if not self.validar_email(email):
            raise ValueError("❌ Email inválido. Debe contener '@' y un dominio válido.")
        
        self._nombre = nombre           
        self._telefono = telefono
        self._email = email
        self._direccion = direccion

    # Validaciones
    @staticmethod
    def validar_nombre(nombre):
        return bool(nombre.strip())   # True si no está vacío

    @staticmethod
    def validar_email(email):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, email)

    @staticmethod
    def validar_telefono(telefono):
        return telefono.isdigit() and len(telefono) >= 7

    # Getters
    def get_nombre(self): return self._nombre
    def get_telefono(self): return self._telefono
    def get_email(self): return self._email
    def get_direccion(self): return self._direccion

    # Setters con validación
    def set_nombre(self, nombre):
        if not self.validar_nombre(nombre):
            raise ValueError("⚠️ El nombre no puede estar vacío.")
        self._nombre = nombre

    def set_telefono(self, telefono):
        if not self.validar_telefono(telefono):
            raise ValueError("⚠️ Teléfono inválido. Solo dígitos y mínimo 7 caracteres.")
        self._telefono = telefono

    def set_email(self, email):
        if not self.validar_email(email):
            raise ValueError("⚠️ Email inválido. Formato incorrecto.")
        self._email = email

    def set_direccion(self, direccion): 
        self._direccion = direccion

    # Representación
    def __str__(self):
        return (f"{self._nombre:<20} | " 
                f"{self._telefono:<12} | "
                f"{self._email:<25} | "
                f"{self._direccion:<30}")