from random import *
def main () :
    times = 0
    cont = 'y'
    dice = die ()
    while cont=='y' :
        times = times + 1
        print(diced(dice))
        print ("You rolled a - " + str(y) + " and " + str(x) + ".")         #find way to check
        print ("You have played " + str(times) + " times.")
        cont = input ("Would you like this to run again? (y/n) - ")

def diced (numOfDice) :


#add funcs here to call on the seperate dies and add em together


def dice1 () :
    a = '  ------- '
    b = ' |       |'
    c = ' |   *   |'
    return (a + '\n' + b + '\n' + c + '\n' + b + '\n' + a)

def dice2 () :
    a = '  ------- '
    b = ' |       |'
    c = ' | *  *  |'
    return (a + '\n' + b + '\n' + c + '\n' + b + '\n' + a)

#here add funcs to return dice3 4 5 and 6



def randNum () :
    z = randint(1,6)
    return (z)

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
