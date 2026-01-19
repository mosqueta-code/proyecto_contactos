import unittest
from contacto import Contacto
from gestorcontactos import GestorContactos

class TestContactoValidaciones(unittest.TestCase):
    def test_creacion_valida(self):
        c = Contacto("Ana Pérez", "1234567", "ana.perez@mail.com", "Pasaje Ramos 75")
        self.assertEqual(c.get_nombre(), "Ana Pérez")
        self.assertEqual(c.get_telefono(), "1234567")
        self.assertEqual(c.get_email(), "ana.perez@mail.com")
        self.assertEqual(c.get_direccion(), "Pasaje Ramos 75")

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError) as ctx:
            Contacto("", "1234567", "ana@mail.com", "Dirección")
        self.assertIn("nombre no puede estar vacío", str(ctx.exception).lower())

    def test_telefono_no_digitos(self):
        with self.assertRaises(ValueError) as ctx:
            Contacto("Ana", "12ab567", "ana@mail.com", "Dirección")
        self.assertIn("teléfono inválido", str(ctx.exception).lower())

    def test_telefono_corto(self):
        with self.assertRaises(ValueError):
            Contacto("Ana", "12345", "ana@mail.com", "Dirección")

    def test_email_sin_arroba(self):
        with self.assertRaises(ValueError) as ctx:
            Contacto("Ana", "1234567", "correo_invalido", "Dirección")
        self.assertIn("email inválido", str(ctx.exception).lower())

    def test_email_sin_dominio(self):
        with self.assertRaises(ValueError):
            Contacto("Ana", "1234567", "ana@", "Dirección")

    def test_email_sin_tld(self):
        with self.assertRaises(ValueError):
            Contacto("Ana", "1234567", "ana@mail", "Dirección")

    def test_setters_validos(self):
        c = Contacto("Ana", "1234567", "ana@mail.com", "Dirección")
        c.set_nombre("Ana María")
        c.set_telefono("7654321")
        c.set_email("ana.maria@mail.com")
        c.set_direccion("Nueva Dirección 123")
        self.assertEqual(c.get_nombre(), "Ana María")
        self.assertEqual(c.get_telefono(), "7654321")
        self.assertEqual(c.get_email(), "ana.maria@mail.com")
        self.assertEqual(c.get_direccion(), "Nueva Dirección 123")

    def test_set_nombre_vacio(self):
        c = Contacto("Ana", "1234567", "ana@mail.com", "Dirección")
        with self.assertRaises(ValueError) as ctx:
            c.set_nombre("   ")
        self.assertIn("nombre no puede estar vacío", str(ctx.exception).lower())

    def test_set_telefono_invalido(self):
        c = Contacto("Ana", "1234567", "ana@mail.com", "Dirección")
        with self.assertRaises(ValueError):
            c.set_telefono("abc1234")
        with self.assertRaises(ValueError):
            c.set_telefono("123")  # demasiado corto

    def test_set_email_invalido(self):
        c = Contacto("Ana", "1234567", "ana@mail.com", "Dirección")
        with self.assertRaises(ValueError):
            c.set_email("ana@")
        with self.assertRaises(ValueError):
            c.set_email("ana.mail.com")


class TestContactoStr(unittest.TestCase):
    def test_formato_str_columnas(self):
        c = Contacto("Ana", "1234567", "ana@mail.com", "Dirección")
        s = str(c)
        # Verifica que contenga separadores y los campos
        self.assertIn("|", s)
        self.assertIn("Ana", s)
        self.assertIn("1234567", s)
        self.assertIn("ana@mail.com", s)
        self.assertIn("Dirección", s)
        # Verifica que haya exactamente 3 separadores (4 columnas)
        self.assertEqual(s.count("|"), 3)


class TestGestorContactos(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorContactos()
        self.c1 = Contacto("Ana", "1111111", "ana@mail.com", "Dir 1")
        self.c2 = Contacto("Luis", "2222222", "luis@mail.com", "Dir 2")
        self.c3 = Contacto("Carla", "3333333", "carla@mail.com", "Dir 3")

    def test_agregar_contacto(self):
        ok = self.gestor.agregar_contacto(self.c1)
        self.assertTrue(ok)
        self.assertEqual(len(self.gestor.contactos), 1)

    def test_agregar_contacto_duplicado_por_telefono(self):
        self.gestor.agregar_contacto(self.c1)
        duplicado = Contacto("Ana Duplicada", "1111111", "otro@mail.com", "Dir X")
        ok = self.gestor.agregar_contacto(duplicado)
        self.assertFalse(ok)
        self.assertEqual(len(self.gestor.contactos), 1)

    def test_editar_contacto_nombre(self):
        self.gestor.agregar_contacto(self.c1)
        ok = self.gestor.editar_contacto("Ana", nuevo_nombre="Ana María")
        self.assertTrue(ok)
        self.assertEqual(self.gestor.contactos[0].get_nombre(), "Ana María")

    def test_editar_contacto_telefono_valido(self):
        self.gestor.agregar_contacto(self.c1)
        ok = self.gestor.editar_contacto("Ana", nuevo_telefono="7654321")
        self.assertTrue(ok)
        self.assertEqual(self.gestor.contactos[0].get_telefono(), "7654321")

    def test_editar_contacto_email_valido(self):
        self.gestor.agregar_contacto(self.c1)
        ok = self.gestor.editar_contacto("Ana", nuevo_email="ana.perez@mail.com")
        self.assertTrue(ok)
        self.assertEqual(self.gestor.contactos[0].get_email(), "ana.perez@mail.com")

    def test_editar_contacto_inexistente(self):
        self.gestor.agregar_contacto(self.c1)
        ok = self.gestor.editar_contacto("NoExiste", nuevo_nombre="X")
        self.assertFalse(ok)

    def test_editar_contacto_con_datos_invalidos_lanza_error(self):
        self.gestor.agregar_contacto(self.c1)
        # Nombre vacío
        with self.assertRaises(ValueError):
            self.gestor.editar_contacto("Ana", nuevo_nombre="   ")
        # Teléfono inválido
        with self.assertRaises(ValueError):
            self.gestor.editar_contacto("Ana", nuevo_telefono="12ab")
        # Email inválido
        with self.assertRaises(ValueError):
            self.gestor.editar_contacto("Ana", nuevo_email="correo_invalido")

    def test_eliminar_contacto(self):
        self.gestor.agregar_contacto(self.c1)
        ok = self.gestor.eliminar_contacto("Ana")
        self.assertTrue(ok)
        self.assertEqual(len(self.gestor.contactos), 0)

    def test_eliminar_contacto_inexistente(self):
        self.gestor.agregar_contacto(self.c1)
        ok = self.gestor.eliminar_contacto("NoExiste")
        self.assertFalse(ok)
        self.assertEqual(len(self.gestor.contactos), 1)

    def test_buscar_por_nombre_coincide_exactamente(self):
        self.gestor.agregar_contacto(self.c1)
        self.gestor.agregar_contacto(self.c2)
        res = self.gestor.buscar_por_nombre("Ana")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].get_nombre(), "Ana")

    def test_buscar_por_nombre_sensible_a_minusculas(self):
        self.gestor.agregar_contacto(self.c1)
        res = self.gestor.buscar_por_nombre("ana")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].get_nombre(), "Ana")

    def test_buscar_por_telefono(self):
        self.gestor.agregar_contacto(self.c1)
        self.gestor.agregar_contacto(self.c2)
        res = self.gestor.buscar_por_telefono("2222222")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].get_nombre(), "Luis")

    def test_mostrar_contactos_formateados(self):
        self.gestor.agregar_contacto(self.c1)
        self.gestor.agregar_contacto(self.c2)
        lista = self.gestor.mostrar_contactos()
        self.assertEqual(len(lista), 2)
        # Cada elemento debe ser la representación __str__ del contacto
        self.assertTrue(all("|" in s for s in lista))


if __name__ == "__main__":
    unittest.main()

