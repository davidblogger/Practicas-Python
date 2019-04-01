v = "otro texto"
n = 10
#print("Un texto",v,"y un número",n)

c = "Un texto {} y un número {}".format(v,n)

#print(c)

"""print("{:>30}".format("Palabra"))
print("{:30}".format("Palabra")) #A la izquierda
print("{:^30}".format("Palabra")) #Centrado
print("{:.5}".format("Palabra")) #Truncamiento a 3 caracteres"""


#formateo de numeros enteros, rellenados con espacios
"""print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))"""

#formateo de numeros enteros, rellenados con ceros
"""print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))"""

#Formateo de números flotantes, rellenados con espacios
"""print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))"""

#Formateo de números flotantes, rellenados con ceros
print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))