"""usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos", "Luis", "Fernando"}
administradores = {"Juan", "Marta"}

administradores.discard("Juan")
administradores.add("Marcos")
administradores.add("Luis")

for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "Es <ADMIN>")
    else:
        print(usuario, "NO es admin")  """


caballero = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}
guerrero  = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}  
arquero   = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2} 

caballero['vida'] = guerrero['vida'] * 2    
caballero['defensa'] = guerrero['defensa'] * 2    

guerrero['ataque'] = caballero['ataque'] * 2    
guerrero['alcance'] = caballero['alcance'] * 2   

arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque'] 

arquero['defensa'] = guerrero['defensa'] / 2
arquero['alcance'] = guerrero['alcance'] * 2

"""print("Caballero:\t", caballero)
print("Guerrero:\t", guerrero)
print("Arquero:\t", arquero)"""

tareas = [
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]

print("==Tareas desordenadas==")
for tarea in tareas:
    print(tarea[0], tarea[1])

from collections import deque 

tareas.sort()
#print(tareas) 

cola = deque()
for tarea in tareas:
    cola.append(tarea[1])  

print("\n==Tareas ordenadas==")
for tarea in cola:
    print(tarea)    

print(cola.popleft()) 
print(cola.popleft())  