pila = [3,4,5]
pila.append(6)
pila.append(7)

pila.pop() #Borra el ultimo elemento ingresado en la pila

#print(pila)


#Colas

from collections import deque
cola = deque()

cola = deque(['David', 'Juan', 'Miguel'])
cola.append('Maria')
cola.append('Arnaldo')

#print(cola.popleft())

p = cola.popleft()

print(p)