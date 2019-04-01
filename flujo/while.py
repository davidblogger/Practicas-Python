"""c = 0
while c  <= 5:
    c+=1
    print("c vale", c)
else:
    print("Se ha completado toda la iteracion y c vale",c)"""

"""c = 0
while c  <= 5:
    c+=1
    if (c == 4):
        print("Rompemos el bucle cuando c vale",c)
        break
    print("c vale", c)
else:
    print("Se ha completado toda la iteracion y c vale",c)"""

"""c = 0
while c  <= 5:
    c+=1
    if (c == 4):
        print("Continuamos con la siguente iteracion",c)
        continue
    print("c vale", c)
else:
    print("Se ha completado toda la iteracion y c vale",c)"""

print("bienvenido al menu interactivo")
while(True):
    print("Que quieres hacer? escribe una opcion 1) Saludar 2) sumar 2 numeros 3) salir""") 
    opcion = input()  
    if opcion == '1':
        print("hola")
    elif opcion == '2':
        n1 = float(input("Introduce el primer numero: ")) 
        n2 = float(input("Introduce el segundo numero: "))
        print("El resultado de la suma es: ", n1+n2)  
    elif opcion == '3':
        print("Hasta luego")   
        break
    else:
        print("comando desconocido")                     

