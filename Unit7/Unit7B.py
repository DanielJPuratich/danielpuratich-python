import Unit7Classes as c

d = c.pet('13', 'Leo', 'Golden Retriever')
print(c.pet.getName(d))
print(c.pet.getBreed(d) + '\n')

d = c.dog('13','Leo','Golden Retriever','Swimming')
print(c.dog.info(d) + '\n')
