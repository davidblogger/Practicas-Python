#conjunto = set()

conjunto = {1,2,3}
#print(conjunto)

conjunto.add(0)
conjunto.add('H')

#print(conjunto)

l = [1,2,3,3,2,1]
c = set(l)
#print(c)

lista = [1,2,3,3,2,1]
lista = list( set( lista ) )
#print(lista)

letras = "Al pan pan y al vino vino"
print(set(letras))
