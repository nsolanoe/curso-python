#calculadora
primerValor = int(input("ingrese el primer valor: "))
segundoValor = int(input("ingrese el segundo valor: "))

operacion = input("que operacion desea realizar: ")

if operacion == "+" :
    print("su resultado es:", primerValor + segundoValor)
elif operacion == "-" :
    print("su resultado es:",primerValor - segundoValor)
elif operacion == "*" :
    print("su resultado es:",primerValor * segundoValor)
elif operacion == "/" :
    print("su resultado es:",primerValor / segundoValor)
else:
    print("no es operacion matematica")
                    
