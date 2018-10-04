def Main () :
    myString = str(input("Enter any string - "))
    print ("Your string is - " + myString )

    print ("Your string without vowels is - " + deVowel(myString))
    print ()

    g = [0] * 4
    g [0] = float(input("Enter a number - "))
    g [1] = float(input("Enter a number - "))
    g [2] = float(input("Enter a number - "))
    g [3] = float(input("Enter a number - "))
    m = float(input("What do you want to multiply by? - "))

    print ("Your average grades using a for loop equals " + mathStuff(g , m))
    print ()

    num1 = str(input ("Put in your best grade? - "))
    num2 = str(input ("Put in your second best grade? - "))
    num3 = str(input ("Put in your third best grade? - "))
    num4 = str(input ("Put in your fourth best grade? - "))
    List1 = [0] * 4
    List1 [0] = num1
    List1 [1] = num2
    List1 [2] = num3
    List1 [3] = num4

    print ("The average of your four best grades using a for loop is - " + avgGrade(List1) + "%")
#=============================================================================================================
def deVowel (myString) :
    myString2 = myString
    myStringV = ""
    for x in myString2 :
        if (x == "a" or x=="e" or x=="i" or x=="o" or x=="u"or x=="A" or x=="E" or x=="O" or x=="U") :
            y = 69
        else :
            myStringV = myStringV + x
    return (myStringV)
#=============================================================================================================
def mathStuff (g , m) :
    Listf = [] * 4
    for x in g :
        Listf.append(float(x) * float(m))
    return (str(Listf))
#=============================================================================================================
def avgGrade (List1) :
    Val = float("0")
    for x in List1 :
        Val = float(Val) + int(x)
    Avg = float(Val) / 4
    return (str(Avg))
#==============================================================================================================
Main ()
