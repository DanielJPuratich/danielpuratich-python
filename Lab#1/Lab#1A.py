def Main () :
    schoolYearNum = int(input("What number grade are you in? - "))
    print ("You are " + yearsInSchool(schoolYearNum))
    print ()

    num1 = float(input ("Put in your best grade? - "))
    num2 = float(input ("Put in your second best grade? - "))
    num3 = float(input ("Put in your third best grade? - "))
    num4 = float(input ("Put in your fourth best grade? - "))
    
    print ("Your grade average is " + calcAverageGrade(num1, num2, num3, num4) + "%.")
    print ()

    print ("Your letter grade average is " + getLetterGrade (num1, num2, num3, num4) + ".")
    print ()

    print ("You are " + passOrFail(num1, num2, num3, num4) + ".")
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
def calcAverageGrade (num1, num2, num3, num4) :
    List1 = [0] * 4
    List1 [0] = num1
    List1 [1] = num2
    List1 [2] = num3
    List1 [3] = num4

    ListL = len (List1)
    ListA = List1.pop (0) + List1.pop (0) + List1.pop (0) + List1.pop (0)
    Gpa = ListA / ListL
    Gpa2 = str(Gpa)
    return (Gpa2)
#============================================================================================================
def getLetterGrade (num1, num2, num3, num4) :
    Avg = (num1 + num2 + num3 + num4) / 4

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

def passOrFail (num1, num2, num3, num4) :
    Avg = (num1 + num2 + num3 + num4) / 4
    if int(Avg) > 70:
        return (str("passing"))
    else:
        return (str("failling"))
#============================================================================================================
Main ()
