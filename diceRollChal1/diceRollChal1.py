from random import *
def main () :
    num1 = int(input('Number of first dice - '))
    num2 = int(input('Number of second dice - '))
    cont = 'y'
    times = 0
    while cont=='y' :
        times = times + 1

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
        print(a + "\n" + b + "\n" + c + "\n" + d + "\n" + a)
        if x==num1 and y==num2 :
            complete(times , num1 , num2)
            break

def complete (times , num1 , num2) :
    print ("It took you " + str(times) + " to roll a " + str(num1) + " and a " + str(num2) + "." )






main ()
