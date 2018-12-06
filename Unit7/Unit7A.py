import Unit7Classes as c

d = c.pet('13', 'Leo', 'Golden Retriever')
print(c.pet.what(d))
print(c.pet.getName(d))
print(c.pet.getBreed(d) + '\n')

g = c.pet('7', 'insert cat name', 'some cat breed idk any')
print(c.pet.getName(g))
print(c.pet.getBreed(g))
print(c.pet.what(g) + '\n')

h = c.cage('Snake', 'True')
print(c.cage.getBreed(h))
print(c.cage.getDanger(h))
print(c.cage.what(h) + '\n')

j = c.cage('Rat', 'False')
print(c.cage.getBreed(j))
print(c.cage.getDanger(j))
print(c.cage.what(j))
