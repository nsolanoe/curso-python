"""
Crear una clase Gato que tenga 2 atributos, nombre y sonido. 
También agregar un método que permita saludar, 
en este método indicar que clase es a la que pertenece y cual es su sonido.
Crear una clase Perro con los mismos métodos y atributos del Gato, 
la particularidad es que este debe indicar en el método saludo, que es un perro y su sonido.
"""
# Realizado por Nicolás Solano



class Gato:
    def __init__(self, nombre, sonido):
      self.nombre = nombre
      self.sonido = sonido

    def gato(self):
        return f"Es de la clase Gato, se llama {self.nombre} y  su sonido es: {self.sonido}"

class Perro(Gato) :
    def __init__(self, nombre, sonido):
     self.nombre = nombre
     self.sonido = sonido

    def perro(self):
      return f"Es de la clase Perro, se llama {self.nombre} y  su sonido es: {self.sonido}"


animal1 = Gato("Pelusa", "miauuu")
animal2 = Perro("Firulais", "waf waf")

print(animal1.gato())
print(animal2.perro())

