from random import *
def main () :

    times = 0
    roll2 = 0
    roll3 = 0
    roll4 = 0
    roll5 = 0
    roll6 = 0
    roll7 = 0
    roll8 = 0
    roll9 = 0
    roll10 = 0
    roll11 = 0
    roll12 = 0

    while times<1000 :
        times = times + 1
        dice = whichDice ()
        if dice==2 :
            roll2 = roll2 + 1
        elif dice==3 :
            roll3 = roll3 + 1
        elif dice==4 :
            roll4 = roll4 + 1
        elif dice==5 :
            roll5 = roll5 + 1
        elif dice==6 :
            roll6 = roll6 + 1
        elif dice==7 :
            roll7 = roll7 + 1
        elif dice==8 :
            roll8 = roll8 + 1
        elif dice==9 :
            roll9 = roll9 + 1
        elif dice==10 :
            roll10 = roll10 + 1
        elif dice==11 :
            roll11 = roll11 + 1
        elif dice==12 :
            roll12 = roll12 + 1

    calcRolls (roll2 , roll3 , roll4 , roll5 , roll6, roll7 , roll8 , roll9 , roll10 , roll11 , roll12)



#=======================================================================================================================
def whichDice () :
    x = randint(1,6)
    y = randint(1,6)
    a = ' -------   ------- '

    if x==1 or x==2 :
        ba = '|       |'
    elif x==3 :
        ba = '|   *   |'
    elif x==4 or x==5 or x==6 :
        ba = '| *  *  |'

    if x==1 or x==3 or x==5 :
        ca = '|   *   |'
    elif x==4 :
        ca = '|       |'
    elif x==2 or x==6 :
        ca = '| *  *  |'

    if x==1 or x==2 :
        da = '|       |'
    elif x==3 :
        da = '|   *   |'
    elif x==4 or x==5 or x==6 :
        da = '| *  *  |'

    if y==1 or y==2 :
        bb = ' |       |'
    elif y==3 :
        bb = ' |   *   |'
    elif y==4 or y==5 or y==6 :
        bb = ' | *  *  |'

    if y==1 or y==3 or y==5 :
        cb = ' |   *   |'
    elif y==4 :
        cb = ' |       |'
    elif y==2 or y==6 :
        cb = ' | *  *  |'

    if y==1 or y==2 :
        db = ' |       |'
    elif y==3 :
        db = ' |   *   |'
    elif y==4 or y==5 or y==6 :
        db = ' | *  *  |'

    b = ba + bb
    c = ca + cb
    d = da + db
    print (a + "\n" + b + "\n" + c + "\n" + d + "\n" + a)
    z = x + y
    return (z)

def calcRolls (r2 , r3 , r4 , r5 , r6 , r7 , r8 , r9 , r10 , r11 , r12) :
    t2 = round((r2 / 1000) * 100)
    t3 = round((r3 / 1000) * 100)
    t4 = round((r4 / 1000) * 100)
    t5 = round((r5 / 1000) * 100)
    t6 = round((r6 / 1000) * 100)
    t7 = round((r7 / 1000) * 100)
    t8 = round((r8 / 1000) * 100)
    t9 = round((r9 / 1000) * 100)
    t10 = round((r10 / 1000) * 100)
    t11 = round((r11 / 1000) * 100)
    t12 = round((r12 / 1000) * 100)

    print ("Two was rolled " + str(r2) + " times, which is " + str(t2) + " percent.")
    print ("Three was rolled " + str(r3) + " times, which is " + str(t3) + " percent.")
    print ("Four was rolled " + str(r4) + " times, which is " + str(t4) + " percent.")
    print ("Five was rolled " + str(r5) + " times, which is " + str(t5) + " percent.")
    print ("Six was rolled " + str(r6) + " times, which is " + str(t6) + " percent.")
    print ("Seven was rolled " + str(r7) + " times, which is " + str(t7) + " percent.")
    print ("Eight was rolled " + str(r8) + " times, which is " + str(t8) + " percent.")
    print ("Nine was rolled " + str(r9) + " times, which is " + str(t9) + " percent.")
    print ("Ten was rolled " + str(r10) + " times, which is " + str(t10) + " percent.")
    print ("Elleven was rolled " + str(r11) + " times, which is " + str(t11) + " percent.")
    print ("Twelve was rolled " + str(r12) + " times, which is " + str(t12) + " percent.")



main ()
