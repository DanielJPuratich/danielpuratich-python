def main () :
    t = int(input("How far would like the loop to go? - "))
    func1 (t)
    print ()

    list1 = [0] * 5
    list1 [0] = int(input("Input a number - "))
    list1 [1] = int(input("Input a number - "))
    list1 [2] = int(input("Input a number - "))
    list1 [3] = int(input("Input a number - "))
    list1 [4] = int(input("Input a number - "))
    m = int(input("Input a multiplier - "))
    func2 (list1, m)
    print ()

    #func3 ()
    print ()

    #func4 ()
    print()
#=======================================================================================================================
def func1 (t) :
    for x in range(1,t) :
        y = int(x) + 10
        y2 = str(y)
        x2 = str(x)
        print (x2 + " + 10 = " + y2)
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
#def func3 () :
#=======================================================================================================================
#def func4 () :
#=======================================================================================================================
main ()
