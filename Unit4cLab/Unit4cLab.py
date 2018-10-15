def main () :        #start of code, is called on at bottom of script
    Stars ()         #calls the function that runs prints a 7x7 cube of stars
    print ()         #print statement to create a division and make the print out look simpler
    starStripe ()    #calls the function which prints alternating rows of stars and stripes
    print ()         #print statement to create a division and make the print out look simpler
    numbs ()         #calls the function which prints numbers in ascending order
    print ()         #print statement to create a division and make the print out look simpler
#-------------------------------------------------------------------------------------------------------------------
    chal1 ()         #calls the function which prints the first challenge (a ox of stars with hyphens inside)
    print ()         #print statement to create a division and make the print out look simpler
    chal2 ()         #calls the function which prints second chal, numbers ascending and then descending at 7

#===================================================================================================================

def Stars () :                  #is called on by main
    for x in range(0,7) :       # runs the following print statement 7 times
        print (" *" * 7)        # prints a * 7 times in one row
#-------------------------------------------------------------------------------------------------------------------
def starStripe () :                  # is called on by main
    for x in range(0, 6) :           #runs this 6 times changing the value of x each time
        if (x%2 == 0) :              # if x is even run the following
            print (" *" * 6)         #print 1 row of *s
        else :                       #if x isnt even run the following
            print (" -" * 6)         #print a row of hyphens
#--------------------------------------------------------------------------------------------------------------------
def numbs () :                   #is called on by main
    for x in range(1,8) :        #goes through loop setting x to 1,2,3 .... each time through
        print (str(x) * x)       #prints the x, the number of times x is equal
#--------------------------------------------------------------------------------------------------------------------
def chal1 () :                                       #is called by main
    for x in range(0,7) :                            #runs this loop 7 times settng x to each value each time
        if x==0 :                                    #if its the first run and x is set to 0 run the following
            print (" *" *7)                          #prints a row of stars
        elif x==1 or x==2 or x==3 or x==4 or x==5 :  #if x is 12345 run the following
            print (" *" + " -" * 5 + " *")           #prints a row of hyphens with stars on outside
        else :                                       #if none of the following are true
            print (" *" *7)                          #prints a row of stars
#--------------------------------------------------------------------------------------------------------------------
def chal2 () :                        # is called on by main
    for y in (1,3) :                  # runs this loop twice one with y==1 and the other with it y==2
        for x in range(1,8) :         # runs loop 7 times with x equalling the coresponding value
            if y == 1 :               # if y==1 then
                print (str(x) * x)    #print the x value the number of times x is
            else :                    #if y=!1 then
                y = x -7              # y will equal x minus 7
                y2 = y * -1           #y2 is y inverted
                print(str(y2) * y2)   #prints y invetered multiplied by the number of times y2 is

#=====================================================================================================================

main ()              # after all fuctions have been defined, activates main fuction which will activate other function


