calificacion = float(input("Ingrese su calificación: "))

if calificacion >= 9 and calificacion <= 10:
    print("felicitaciones tienes una A")
elif calificacion >= 8 and calificacion < 9:
    print("muy bien tienes una B")
elif calificacion >= 7 and calificacion < 8:
    print("tienes una C")
elif calificacion >= 6 and calificacion < 7:
    print("puedes mejorar tienes una D")
elif calificacion  >= 0 and calificacion <6:
    print("reprobaste tienes una F")
else:
    print("valor no permitido")

 
