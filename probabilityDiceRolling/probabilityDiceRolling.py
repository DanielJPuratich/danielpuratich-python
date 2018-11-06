from random import randint
def main () :
    print ("The program will run unti it gets the number you input 5 times in a row")
    num = int(input("Input a number between 1 and 6 - "))
    x = 0
    times = 0
    while x==0 :
        times = times + 1
        b = randint(1,6)
        if b==num :
            c = randint(1,6)
            if c==num :
                d = randint(1,6)
                if d==num :
                    e = randint(1,6)
                    if e==num :
                        f = randint(1,6)
                        if f==num :
                            g = randint(1,6)
                            if g==num :
                                h = randint(1,6)
                                if h==num :
                                    i = randint(1,6)
                                    if i==num :
                                        yay (num, times)
                                        break

def yay (num, times) :

    print ("It took " + str(times) + " to roll a " + str(num))





main ()
