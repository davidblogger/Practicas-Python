def realizar_operacion(operacion,numero1,numero2):
    if operacion == 1:
        return numero1 + numero2
    elif operacion == 2:
        return numero1 - numero2
    elif operacion == 3:
        return numero1 * numero2
    else:
        return numero1 / numero2



print("Bienvenidos a la calculadora en Python")
while True:
    print("Estas son la operaciones que puedes realizar")
    print("1 - suma")
    print("2 - resta")
    print("3 - multiplicacion")
    print("4 - division")

    try:
        operacion = int(input("introduce el numero de operacion que quieres realizar: "))
        numero1 = int(input("introduce el primer numero: "))
        numero2 = int(input("introduce el segundo numero: "))
    except NameError:
        print("Por favor introduce solo numeros")
    else:
        if operacion < 1 or operacion > 4:
            print("Ese no es un numero de operacion valido")
            print("")
            continue
        resultado = realizar_operacion(operacion,numero1,numero2)
        print("El resultado es: " + str(resultado))
        continuar = raw_input("Deseas continuar si/no ")
        print("")
        print("")

        if continuar != "si":
            break

print("Gracias por usar nuestra calculadora!!!")
