from random import *
def main () :
    times = 0
    # roll2 = 0
    # roll3 = 0
    # roll4 = 0
    # roll5 = 0
    # roll6 = 0
    while times<1000 :
        dice = whichDice ()
        times = times + 1
    #     elif dice==2 :
    #         roll2 = roll2 + 1
    #     elif dice==3 :
    #         roll3 = roll3 + 1
    #     elif dice==4 :
    #         roll4 = roll4 + 1
    #     elif dice==5 :
    #         roll5 = roll5 + 1
    #     elif dice==6 :
    #         roll6 = roll6 + 1
    # calcRolls (roll1 , roll2 , roll3 , roll4 , roll5 , roll6)



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

def calcRolls () :



main ()
