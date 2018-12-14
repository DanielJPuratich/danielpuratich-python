import Unit6BList as dict
from random import randint
a = input("Enter birthday month and date - ")
y,x = dict.asd(a)
for b in dict.weekends :
    if b==x :
        for c in dict.weekends[b] :
            if c==int(y) :
                print("Your Birthday is on a weekend!")
                dict.d = 0
if dict.d==1 :
    print("Your birthday isn't a weekend! (or you can't spell)")
j = dict.aBunchOfPointlessIfStatements(y , x)
print("Your birthday is: " + j)
exit(randint(69,690))
