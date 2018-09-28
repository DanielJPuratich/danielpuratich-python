def Main () :
    schoolYearNum = int(input("What number grade are you in? - "))
    print ("You are " + yearsInSchool(schoolYearNum))
    print ()

    check3 = str("no")
    check4 = str("no")
    check5 = str("no")
    check6 = str("no")

    num1 = float(input ("Put in your best grade? - "))
    check2 = str(input("Do you want to put in another grade? - "))

    if str(check2) == "yes" :
        num2 = float(input ("Put in your second best grade? - "))
        check3 = str(input("Do you want to put in another grade? - "))
    elif str(check2) == "Yes" :
        num2 = float(input ("Put in your second best grade? - "))
        check3 = str(input("Do you want to put in another grade? - "))
    else:
        num2 = float(num1)

    if str(check3) == "yes" :
        num3 = float(input ("Put in your third best grade? - "))
        check4 = str(input("Do you want to enter another grade? - "))
    elif str(check3) == "Yes" :
        num3 = float(input ("Put in your third best grade? - "))
        check4 = str(input("Do you want to enter another grade? - "))
    else:
        num3 = float((num1 + num2) / (2))

    if str(check4) == "yes" :
        num4 = float(input ("Put in your fourth best grade? - "))
        check5 = str(input("Do you want to enter another grade? - "))
    elif str(check4) == "Yes" :
        num4 = float(input ("Put in your fourth best grade? - "))
        check5 = str(input("Do you want to enter another grade? - "))
    else:
        num4 = float((num1 + num2 + num3) / (3))

    if str(check5) == "yes" :
        num5 = float(input ("Put in your fifth best grade? - "))
        check6 = str(input("Do you want to enter another grade? - "))
    elif str(check5) == "Yes" :
        num5 = float(input ("Put in your fifth best grade? - "))
        check6 = str(input("Do you want to enter another grade? - "))
    else:
        num5 = float((num1 + num2 + num3 + num4) / (4))

    if str(check6) == "yes" :
        num6 = float(input ("Put in your sixth best grade? - "))
    elif str(check6) == "Yes" :
        num6 = float(input ("Put in your sixth best grade? - "))
    else:
        num6 = float((num1 + num2 + num3 + num4 + num5) / (5))

    print ("Your grade average is " + calcAverageGrade(num1, num2, num3, num4, num5, num6) + "%.")
    print ()

    print ("Your letter grade average is " + getLetterGrade (num1, num2, num3, num4, num5, num6) + ".")
    print ()

    print ("You are " + passOrFail(num1, num2, num3, num4, num5, num6) + ".")
#============================================================================================================
def yearsInSchool (numGrade) :
    if numGrade == 9:
        return (str("a freshman."))
    elif numGrade == 10:
        return (str("a spohmore."))
    elif numGrade == 11:
        return (str("a junior."))
    elif numGrade == 12:
        return (str("a senior."))
    else:
        return (str("not in highschool."))
#============================================================================================================
def calcAverageGrade (num1, num2, num3, num4, num5, num6) :
    List1 = [0] * 6
    List1 [0] = num1
    List1 [1] = num2
    List1 [2] = num3
    List1 [3] = num4
    List1 [4] = num5
    List1 [5] = num6

    ListL = len (List1)
    ListA = List1.pop (0) + List1.pop (0) + List1.pop (0) + List1.pop (0) + List1.pop (0) + List1.pop (0)
    Gpa = ListA / ListL
    Gpa2 = str(Gpa)
    return (Gpa2)
#============================================================================================================
def getLetterGrade (num1, num2, num3, num4, num5, num6) :
    List1 = [0] * 6
    List1 [0] = num1
    List1 [1] = num2
    List1 [2] = num3
    List1 [3] = num4
    List1 [4] = num5
    List1 [5] = num6
    ListL = len (List1)
    Avg = (num1 + num2 + num3 + num4 + num5 + num6) / ListL

    if int(Avg) > 90:
       return (str("A"))

    elif int(Avg) > 80:
        return (str("B"))

    elif int(Avg) > 70:
        return (str("C"))

    elif int(Avg) > 60:
        return (str("D"))

    else:
        return (str("F"))

def passOrFail (num1, num2, num3, num4, num5, num6) :
    Avg = (num1 + num2 + num3 + num4 + num5 + num6) / 6
    if int(Avg) > 70:
        return (str("passing"))
    else:
        return (str("failling"))
#============================================================================================================
Main ()
