

nota = float(input("ingrese aqui su nota"))

if nota <= 10 and nota >=9:
    print("excelente", nota)
elif nota < 9 and nota >= 8 :
    print("muy bueno", nota)
elif nota < 8 and nota >= 7:
    print("bueno",nota) 
elif nota < 7 and nota >= 0:
    print("reprobado")
else:
    print("ingrese una nora valida")
