def main () :
    #shoppingCart = createCustomList ()
    shoppingCart = [['tooth paste','q-tips','milk'],['milk','candy','apples'],['paper','pencils','q-tips']]
    print ("oldCart - " + str(shoppingCart))
    print ()
    print ("newCart - " + combineLists(shoppingCart))
    print ()
    print ("the number of q-tips is - " + countTips(shoppingCart))
    print ()
    print ("Shopping cart with milk - " + str(drinkMoreMilk(shoppingCart)))
    listWithMilk = drinkMoreMilk(shoppingCart)
    print ()
    print ("Whatever milk and cookies challenge is - " + milkCookies(listWithMilk))
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
def drinkMoreMilk (cart) :
    x = int(0)
    newCart = []
    for group in cart :
        for item in group :
            if item=='milk' or item=='Milk' :
                x = x + 1
    if x==0 :
        newCart = cart + [['milk']]
    else :
        newCart = cart
    return (newCart)
#=======================================================================================================================================================================================
def milkCookies (cart) :                                   #this is the only part that doesn't work
    #try :
    #cart.remove ('milk')
    #cart = cart +['milk and cookies']
        #milkCookies(cart)
    #except ValueError :
        #pass
    return ('yeah, i cant figure this out')
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
