import unittest

class Materia:
    def __init__(self, nombre, profesores):
        self.__nombre__ = nombre
        self.__profesores__ = profesores

    def obtener_profesores(self):
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre


class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__

class Test_materia(unittest.TestCase):
    def test_constructor(self):
        materia = Materia("Matematicas",["Profesor1","Profesor2"])
        self.assertEqual(materia.obtener_profesores(), ["Profesor1", "Profesor2"])

    def test_obtener_profesores(self):
        materia = Materia("Matemáticas", ["Profesor1", "Profesor2"])
        self.assertEqual(materia.obtener_profesores(), ["Profesor1", "Profesor2"])

    def test_cambiar_nombre(self):
        materia = Materia("Matemáticas", ["Profesor1", "Profesor2"])
        materia.cambiar_nombre("Física")
        self.assertEqual(materia.__nombre__, "Física")

class Test_profesor(unittest.TestCase):

    def test_constructor(self):
        profesor = Profesor("Juan", "Docente", 12345)
        self.assertEqual(profesor.obtener_nombre(), "Juan")
        self.assertEqual(profesor.obtener_cargo(), "Docente")
        self.assertEqual(profesor.obtener_legajo(), 12345)

    def test_obtener_nombre(self):
        profesor = Profesor("Juan", "Docente", 12345)
        self.assertEqual(profesor.obtener_nombre(), "Juan")

    def test_obtener_cargo(self):
        profesor = Profesor("Juan", "Docente", 12345)
        self.assertEqual(profesor.obtener_cargo(), "Docente")

    def test_obtener_legajo(self):
        profesor = Profesor("Juan", "Docente", 12345)
        self.assertEqual(profesor.obtener_legajo(), 12345)

if __name__ == '__main__':
    unittest.main()