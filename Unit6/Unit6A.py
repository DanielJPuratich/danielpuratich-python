def main () :
    dict = {'tldr':'too long didnt read','smh':'shake my head','afk':'away from keyboard'}
    d = 'y'
    while d=='y' :
        f = input("Would you like to use dictionary or modify dictionary or view dictionary (u/m/v) - ")
        if f=='u' :
            dict = norm(dict)
        elif f=='m' :
            dict = mod(dict)
        else :
            dict = view(dict)
#===============================================================
def norm (dict) :
    x='y'
    while x=='y' :
        d = input('Put in code - ')
        if d in dict :
            print(dict[d])
        else :
            print("This isnt in the dictionary currently")
            n = input("Would you like to add it to the dictionary? (y/n) - ")
            if n=='y' :
                c = input("What does that stand for - ")
                dict[d] = c

        x = input('Would you like to read another abreviattion (y/n) - ')
        print()
    return(dict)
#==========================================================================
def mod (dict) :
    x = 'y'
    while x=='y' :
        f = input("Would you like to remove or edit an entrey (r/e) - ")
        if f=='r' :
            l = input("What abreviation would you like to remove? - ")
            del dict[l]
        elif f=='e' :
            g = input("What abreviation would you like to edit? - ")
            q = input("What does that abreviation actually stand for? - ")
            del dict[g]
            dict[g] = q
        else :
            print("This isn't valid, please input an r or e for remove and edit!")
        x = input("Would you like to remove another item(y/n) - ")
        print()
    return(dict)
#==========================================================================
def view(dict) :
    for x in dict :
        print(x + ' : ' + dict[x] + '      ', end='')
    print()
    print()
    return (dict)
#==========================================================================
main ()
