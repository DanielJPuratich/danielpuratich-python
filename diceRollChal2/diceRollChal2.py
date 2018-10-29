from random import *
def main () :
    times = 0
    roll1 = 0
    roll2 = 0
    roll3 = 0
    roll4 = 0
    roll5 = 0
    roll6 = 0
    while times<1000 :
        dice = whichDice ()
        times = times + 1
        if dice==1 :
            roll1 = roll1 + 1
        elif dice==2 :
            roll2 = roll2 + 1
        elif dice==3 :
            roll3 = roll3 + 1
        elif dice==4 :
            roll4 = roll4 + 1
        elif dice==5 :
            roll5 = roll5 + 1
        elif dice==6 :
            roll6 = roll6 + 1
    calcRolls (roll1 , roll2 , roll3 , roll4 , roll5 , roll6)

def whichDice () :
    a = ' ------- '
    randnum = randint(1,6)
    if randnum==1 or randnum==2 :
        b = '|       |'
    elif randnum==3 :
        b = '|   *   |'
    elif randnum==4 or randnum==5 or randnum==6 :
        b = '| *  *  |'

    if randnum==1 or randnum==3 or randnum==5 :
        c = '|   *   |'
    elif randnum==4 :
        c = '|       |'
    elif randnum==2 or randnum==6 :
        c = '| *  *  |'

    if randnum==1 or randnum==2 :
        d = '|       |'
    elif randnum==3 :
        d = '|   *   |'
    elif randnum==4 or randnum==5 or randnum==6 :
        d = c = '| *  *  |'

    e = ' ------- '

    print (a + "\n" + b + "\n" + c + "\n" + d + "\n" + e)
    return (randnum)

def calcRolls (r1,r2,r3,r4,r5,r6) :
    t1 = round((r1 / 1000) * 100)
    t2 = round((r2 / 1000) * 100)
    t3 = round((r3 / 1000) * 100)
    t4 = round((r4 / 1000) * 100)
    t5 = round((r5 / 1000) * 100)
    t6 = round((r6 / 1000) * 100)
    print ("One was rolled " + str(r1) + " times, which is " + str(t1) + " percent.")
    print ("Two was rolled " + str(r2) + " times, which is " + str(t2) + " percent.")
    print ("Three was rolled " + str(r3) + " times, which is " + str(t3) + " percent.")
    print ("Four was rolled " + str(r4) + " times, which is " + str(t4) + " percent.")
    print ("Five was rolled " + str(r5) + " times, which is " + str(t5) + " percent.")
    print ("Six was rolled " + str(r6) + " times, which is " + str(t6) + " percent.")

main ()
