vacio = {}
#print(type(vacio))

colores = {'amarillo': 'yellow', 'azul':'blue', 'verde':'green'}
#print(colores['azul'])

edades = {'David': '35', 'Maria': '26', 'Juan': '22'}
#edades['David'] += 1
#print(edades)

#for edad in edades:
    #print(edad)

"""for clave in edades:
    #print(edades[clave]) 
     print(clave,edades[clave]) """

"""for clave, valor in edades.items():
    print(clave,valor)"""


personajes = []
p = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Humano'} 
p = {'Nombre': 'Orco', 'Clase': 'Guerrero', 'Raza': 'Animal'} 
p = {'Nombre': 'Arthas', 'Clase': 'Rey', 'Raza': 'Espada'} 
personajes.append(p)
##print(personajes) 

for p in personajes:
    print(p['Nombre'], p['Clase'], p['Raza'])
