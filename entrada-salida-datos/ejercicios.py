import sys

"""print("{:>20}".format("Hola Mundo"))
print("{:.3}".format("Hola Mundo"))
print("{:^20.1}".format("Hola Mundo"))
print("{:05d}".format(150))
print("{:7d}".format(7887))
print("{:07.3f}".format(20.02))"""


if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print("Error - Filas o columnas incorrectos")
        print("ejemplo - salidas.py [1-9] [1-9]")
    else:
        #Aqui empieza la lógica  
        for f in range(filas):
            print("")
            for c in range(columnas):
                print(" 0 ", end='')
              

else:
    print("Error - Argumentos incorrectos")
    print("ejemplo - salidas.py [1-9] [1-9]")



