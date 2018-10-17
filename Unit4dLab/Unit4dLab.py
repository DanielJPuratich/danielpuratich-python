def main () :                                                                                                           #main calls all functions and holds lists
    shoppingCart = createCustomList ()                                                                                  #if you chose defines list to your choice
    #shoppingCart = [['tooth paste','q-tips','milk'],['milk','candy','apples'],['paper','pencils','q-tips']]             #
    print ("oldCart - " + str(shoppingCart))
    print ()
    print ("newCart - " + combineLists(shoppingCart))
    print ()
    print ("the number of q-tips is - " + countTips(shoppingCart))
    print ()
    print ("Shopping cart with milk - " + drinkMoreMilk(shoppingCart))
#=======================================================================================================================================================================================
def combineLists (origCart) :
    newCart = []
    for group in origCart :
        for item in group :
            if item not in newCart :
                newCart = newCart + [item]
    return (str(newCart))
#=======================================================================================================================================================================================
def countTips (cart) :
    numtips = int(0)
    for group in cart :
        for item in group :
            if item=='q-tips' :
                numtips = numtips + 1
    return (str(numtips))
#=======================================================================================================================================================================================
def drinkMoreMilk (cart) :                                                                                              #this is the only part that doesnt work
    newCart = []
    if 'milk' in cart :
        newCart = cart + [['milk']]
    else :
        newCart = cart
    return (str(newCart))
#=======================================================================================================================================================================================
def createCustomList () :
    aa = input("Group 1 item 1 - ")
    ab = input("Group 1 item 2 - ")
    ac = input("Group 1 item 3 - ")
    ba = input("Group 2 item 1 - ")
    bb = input("Group 2 item 2 - ")
    bc = input("Group 2 item 3 - ")
    ca = input("Group 3 item 1 - ")
    cb = input("Group 3 item 2 - ")
    cc = input("Group 3 item 3 - ")
    customList = [[aa , ab , ac],[ba , bb , bc],[ca , cb , cc]]
    return (customList)
#=======================================================================================================================================================================================
main ()                                                                                                                 #after everything is defined starts main
