class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones

    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

    def estudiante(self):
        return f"El estudiante {self.nombre} tiene {self.edad}años y esta es su calificacion final: {self.promedio()}"    

estudiante1 = Estudiante("Juan", 20, [7, 8, 9])
estudiante2 = Estudiante("Pedro", 21, [6, 7, 8])

print(estudiante1.estudiante())
print(estudiante2.estudiante())
