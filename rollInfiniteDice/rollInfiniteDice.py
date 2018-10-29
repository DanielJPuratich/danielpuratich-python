from random import *
def main () :
    times = 0
    cont = 'y'
    dice = die ()
    while cont=='y' :
        times = times + 1
        print(diced(dice))
        print ("You have played " + str(times) + " times.")
        cont = input ("Would you like this to run again? (y/n) - ")

def diced (numOfDice) :
    a = "  ------- " * numOfDice
    t = ''
    u = ''
    i = ''
    for num in range(0 , numOfDice) :
        y = randint(1,6)

        if y==1 or y==2 :
            b = ' |       |'
        elif y==3 :
            b = ' |   *   |'
        elif y==4 or y==5 or y==6 :
            b = ' | *  *  |'

        if y==1 or y==3 or y==5 :
            c = ' |   *   |'
        elif y==4 :
            c = ' |       |'
        elif y==2 or y==6 :
            c = ' | *  *  |'

        if y==1 or y==2 :
            d = ' |       |'
        elif y==3 :
            d = ' |   *   |'
        elif y==4 or y==5 or y==6 :
            d = ' | *  *  |'

        t = t + b
        u = u + c
        i = i + d



    return (a + "\n" + t + "\n" + u + "\n" + i + "\n" + a)



def die () :
    w = 'n'
    while w=='n':
        try :
            q = int(input("How many dice do you want to roll? - "))
            if q>0 :
                return (q)
            else :
                print ("This is not a valid number" + '\n')
        except ValueError:
            print ("This is not a valid number" + '\n')







main ()
