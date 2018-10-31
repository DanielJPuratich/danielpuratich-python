from random import *
def main () :
    cont = 'y'
    dice = 5
    while cont=='y' :
        List = [0] * 15
        for x in range(0,3) :
            List = diced(dice , List)
        calcList(List)
        cont = input("Would you like to play again? (y/n) - ")
        print ()

def diced (numOfDice , List) :
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
        List.append(y)

    print (a + "\n" + t + "\n" + u + "\n" + i + "\n" + a)
    return (List)

def calcList (List) :
    num = 0
    for x in List :
        num = num + x
    print ("All your numbers added up equals - " + str(num))

main ()
