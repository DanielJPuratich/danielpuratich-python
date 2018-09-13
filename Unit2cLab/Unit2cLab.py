
print ()
print('Define numList and print it and its length (List)')
numList = [0,1,2,3,4,5,6,7,8,9]
print (numList)
print(len(numList))

print ()
print('Creates subList that only has the first 5 items in numList (Slice)')
subList = numList [0:5]
print (subList)

print()
print ('Takes numList and addes another number to the end of the list called subList1 and prints it (add)')
subList1 = numList + [10]
print (subList1)

print()
print('Appending a new item to subList')
subList.append (5)
print (subList)

print()
print('Append using the + feature')
subList3 = subList + [6]
print (subList3)

print()
print('Create List called myClass with my schedule')
myClass = ['Math', 'PE', 'Physics', 'French', 'Python', 'Ignation Seperation', 'World History', 'English' ]

print()
print('Remove one class')
myClass.remove ('Ignation Seperation')

print()
print('Print favorite class')
favClass = myClass.pop (0)
print (favClass)

print()
print ('Print what my favorite class is')
print("my favorite class is " + favClass )





