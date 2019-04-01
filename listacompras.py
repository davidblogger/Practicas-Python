lista_articulos = list()

def agregar_articulo():
    print()
    articulo = input("nombre del articulo a agregar: ")
    lista_articulos.append(articulo.capitalize())
    print("Articulo agregado")


def remover_articulo():
    print("")
    articulo = input("Nombre del articulo a remover: ")
    lista_articulos.remove(articulo.capitalize())
    print("El articulo ha sido removido")

def ver_articulos():
    print()
    print("*********Lista de Compras********")
    for producto in lista_articulos:
        print(producto)
    print("**********************************")
    print()


print("Bienvenido a la lista de compras")
print()
while True:
    print()
    print("Estas son laa operaciones que puedes realizar")
    print("1- Agregar articulo")
    print("2- Remover articulo")
    print("3- Ver los articulo")
    print("4- Salir ")

    operacion = int(input(": "))
    if operacion == 1:
        agregar_articulo()
    elif operacion == 2:
        remover_articulo()
    elif operacion == 3:
        ver_articulos()
    else:
        break

print()
print("Gracias por usar nuestra aplicacion")
print("Saludos")


