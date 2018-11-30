import Unit6BList as dict
x = input("Enter birthday month - ")
y = int(input("Enter brthday date - "))
for b in dict.weekends :
    if b==x :
        for c in dict.weekends[b] :
            if c==y :
                print("Your Birthday is on a weekend!")
                dict.d = 0
if dict.d==1 :
    print("Your birthday isn't a weekend!")
exit(69)
