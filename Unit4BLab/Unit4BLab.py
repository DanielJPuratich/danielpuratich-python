def main () :
    t = int(input("How far would like the loop to go? - "))
    func1 (t)
    print ()
    #---------------------------------------------------------------
    list1 = [0] * 5
    list1 [0] = int(input("Input a number - "))
    list1 [1] = int(input("Input a number - "))
    list1 [2] = int(input("Input a number - "))
    list1 [3] = int(input("Input a number - "))
    list1 [4] = int(input("Input a number - "))
    m = int(input("Input a multiplier - "))
    func2 (list1, m)
    print ()
    #---------------------------------------------------------------
    times = int(input("How many grades do you want to input? - "))
    gl = []
    for x in range(0 , times) :
        gl.append(input("Enter a grade? - "))
    print ("The average of your grades is - " + func3(gl))
    print ()
    #---------------------------------------------------------------
    print ("You are " + func4(gl))
    print()
    #---------------------------------------------------------------
    print ("Your letter grade is " + func5(gl))
    print()
#=======================================================================================================================
def func1 (t) :
    for x in range(1,t) :
        y = int(x) + 10
        y2 = str(y)
        x2 = str(x)
        print (x2 + " + 10 = " + y2)
        #---------------------------------------------------------------
        y = int(x) * 10
        y2 = str(y)
        x2 = str(x)
        print (x2 + " * 10 = " + y2)
#=======================================================================================================================
def func2 (list1, m) :
    print (list1)
    list2 = []
    for eachItemInList in list1:
        list2.append(int(eachItemInList) * int(m))
    list1 = list2
    print (list1)
#=======================================================================================================================
def func3 (gl) :
    b = len(gl)
    d = 0
    for x in gl :
        d = int(d) + int(x)
    avg = d / b
    avg2 = str(avg)
    return (avg2)
#=======================================================================================================================
def func4 (gl) :
    b = len(gl)
    d = 0
    for x in gl :
        d = int(d) + int(x)
    avg = d / b
    if avg > 70 :
        y = "passing."
    else :
        y = "failling."
    return (y)
#=======================================================================================================================
def func5 (gl) :
    b = len(gl)
    d = 0
    for x in gl :
        d = int(d) + int(x)
    Avg = d / b
    #---------------------------------------------------------------
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
#=======================================================================================================================
main ()
