from random import *
def main () :
    times = 0
    cont = 'y'
    dice = die ()
    while cont=='y' :
        times = times + 1
        diceList = diced(dice)
        print ("You have played " + str(times) + " times.")
        calcDiceProb(diceList , dice)
        cont = input ("Would you like this to run again? (y/n) - ")


def diced (numOfDice) :
    a = "  ------- " * numOfDice
    t = ''
    u = ''
    i = ''
    List = [0] * numOfDice
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

        List.append(y)
        t = t + b
        u = u + c
        i = i + d



    print (a + "\n" + t + "\n" + u + "\n" + i + "\n" + a)
    return (List)

def calcDiceProb (List , numOfDice) :
    roll1 = 0
    roll2 = 0
    roll3 = 0
    roll4 = 0
    roll5 = 0
    roll6 = 0
    for num in List :
        if num==1 :
            roll1 = roll1 + 1
        elif num==2 :
            roll2 = roll2 + 1
        elif num==3 :
            roll3 = roll3 + 1
        elif num==4 :
            roll4 = roll4 + 1
        elif num==5 :
            roll5 = roll5 + 1
        elif num==6 :
            roll6 = roll6 + 1
    t1 = round((roll1 / numOfDice) * 100)
    t2 = round((roll2 / numOfDice) * 100)
    t3 = round((roll3 / numOfDice) * 100)
    t4 = round((roll4 / numOfDice) * 100)
    t5 = round((roll5 / numOfDice) * 100)
    t6 = round((roll6 / numOfDice) * 100)
    print ("One was rolled " + str(roll1) + " times, which is " + str(t1) + " percent.")
    print ("Two was rolled " + str(roll2) + " times, which is " + str(t2) + " percent.")
    print ("Three was rolled " + str(roll3) + " times, which is " + str(t3) + " percent.")
    print ("Four was rolled " + str(roll4) + " times, which is " + str(t4) + " percent.")
    print ("Five was rolled " + str(roll5) + " times, which is " + str(t5) + " percent.")
    print ("Six was rolled " + str(roll6) + " times, which is " + str(t6) + " percent.")



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
