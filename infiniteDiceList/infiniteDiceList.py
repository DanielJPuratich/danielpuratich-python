from random import randint
def main () :
    loop = 'y'
    times = 0
    while loop=='y' :
        perRow = int(input("How many dice per roll? - "))
        times = times + 1
        diceList = diceLists( perRow)
        pridie(diceList)
        loop = input ("Would you like this to run again? (y/n) - ")
        print ("You have played " + str(times) + " times.")


def rand () :
    y = randint (1,6)
    return (y)

def diceLists ( perRow) :
    tb = ' -------  '
    b = '|       | '
    o = '|   *   | '
    t = '| *  *  | '
    finalOut = []
    for x in range(0,perRow) :
        dice = rand ()
        if dice==1 :
            outDice = [tb , b , o , b , tb]
        elif dice==2 :
            outDice = [tb , b , t , b , tb]
        elif dice==3 :
            outDice = [tb , o , o , o , tb]
        elif dice==4 :
            outDice = [tb , t , b , t , tb]
        elif dice==5 :
            outDice = [tb , t , o , t , tb]
        elif dice==6 :
            outDice = [tb , t , t , t , tb]
        finalOut.append(outDice)
    return(finalOut)

#this pridie part of the code is the only part thats not working===============================================================
def pridie (diceLis) :
    #print (diceLis)                                            #for testing, delete later
    for list in range(0 , len(diceLis[0])) :
        for item in range(0 , len(diceLis)) :
            print (diceLis[item][list] , end = '\t')
        print ()
#==============================================================================================================================


main ()
