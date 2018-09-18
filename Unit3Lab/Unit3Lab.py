# calls upon defined item which takes your age, multiplies it by 365 then prints it
def howManyDaysOld () :
    age = input ("How old are you? - ")
    daysOld = (int(age) * 365)
    print ("You are " + str(daysOld) + " days old!")

howManyDaysOld ()
print ()


#================================================================================================================================================================

#Calls defined thing which asks you for your school and subject and then prints them
def schoolSubject () :
    school = input ("What school are you from? - ")
    subject = input ("What is your favorite subject? - ")
    print ("You go to " + str(school) + " and your favorite subject is " + str(subject) + ".")

schoolSubject ()
print ()


#================================================================================================================================================================

#Takes your city and grade input then sends it to defined thing and then prints it in defined thing
def cityGrade ( city , grade ) :
    print ("You've been going to school for " + str(grade) + " years in " + str(city) + ".")


myCity = input ("What is your city? - ")
myGrade = input ("What is your grade? - ")
cityGrade (myCity, int(myGrade))
print ()

#================================================================================================================================================================

#Calls defined random function which takes input of 2 numbers, then finds a random number between them and prints it
from random import *
def randNum () :
    x = input ("What's my start number ? - ")
    y = input ("What's my end number? - ")
    myNumber = randint (int(x) , int(y))
    print (str(myNumber) + " is a random number between " + str(x) + " and " + str(y) + ".")

randNum ()
print ()

#================================================================================================================================================================

#calcuates area and perminter of box
def areaBox ( length , width) :
    area = (int(length) * int(width))
    return (area)

def permBox ( length , width ) :
    perm = ( 2*(int(length)) + 2*(int(width)))
    return (perm)

x = input ("Length of box? - ")
y = input ("Width of box? - ")
print ("A box with a length of " + str(x) + " and a width of " + str(y) + " has an area of " + str((areaBox(x , y))) + ".")
print ("A box with a length of " + str(x) + " and a width of " + str(y) + " has a permieter of " + str((permBox(x , y))) + ".")

#================================================================================================================================================================
