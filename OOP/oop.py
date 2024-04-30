import unittest

class Materia:
    def __init__(self, nombre, profesores,alumnos): #constructor y atributos de la clase materia: nombre y profesor
        self.__nombre__ = nombre 
        self.__profesores__ = profesores
        self.__alumnos__= alumnos

    def obtener_profesores(self): #metodo obtiene los profesores
        return self.__profesores__ #devuelve los profesores

    def cambiar_nombre(self, nombre): #cambia el nombre de la materia
        self.__nombre__ = nombre 

    def obtener_alumnos(self):
        return self.__alumnos__
    
class Profesor:
    def __init__(self, nombre, cargo, legajo): #constructor y atributos de la clase profesor: nombre, cargo y legajo
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self): #metodos de la clase profesor
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__
    
class Alumno:
    def __init__(self, nombre, carrera, legajo):
        self.__nombre__ = nombre
        self.__carrera__ = carrera
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__
    
    def obtener_carrera(self):
        return self.__carrera__
    
    def obtener_legajo(self):
        return self.__legajo__

    
class Test_materia(unittest.TestCase):
    def test_constructor(self):
        nombre = 'Computacion'
        profesores = ['Juan','Francisco']
        alumnos = ['Victoria','Valentina','Celina']
        materia = Materia(nombre, profesores,alumnos)
        self.assertEqual(materia.obtener_profesores(), profesores)
        self.assertEqual(materia.__nombre__, nombre)
        self.assertEqual(materia.obtener_alumnos(),alumnos)


    def test_cambiar_nombre(self):
        nombre = 'Computacion'
        nuevo_nombre = 'Programacion'
        alumnos = ['Victoria','Valentina','Celina']
        materia = Materia(nombre,[],alumnos)
        materia.cambiar_nombre(nuevo_nombre)
        self.assertEqual(materia.__nombre__, nuevo_nombre)

class Test_profesor(unittest.TestCase):
    def test_constructor(self):
        nombre = 'Juan'
        cargo = 'Ayudante de catedra'
        legajo = 123
        profesor = Profesor(nombre,cargo,legajo)
        self.assertEqual(profesor.obtener_nombre(), nombre)
        self.assertEqual(profesor.obtener_cargo(), cargo)
        self.assertEqual(profesor.obtener_legajo(), legajo)

class Test_alumno(unittest.TestCase):
    def test_constructor(self):
        nombre = 'Lucas'
        carrera = 'Ingenieria Informatica'
        legajo = 467
        alumno = Alumno(nombre, carrera, legajo)
        self.assertEqual(alumno.obtener_nombre(), nombre)
        self.assertEqual(alumno.obtener_carrera(), carrera)
        self.assertEqual(alumno.obtener_legajo(), legajo)


if __name__ == '__main__':
    unittest.main()