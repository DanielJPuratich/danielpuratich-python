
numGrade = float(input ("Enter a percentage grade:  "))

if numGrade > 92:
    print ("A")

elif numGrade > 80:
    print ("B")

elif numGrade > 70:
    print ("C")

elif numGrade <70:
    print ("F")


print ("")
userIn = input ("Input your favorite color :  ")
print ("Your favorite color is: " + userIn)

if userIn == "green":
    print ("Trees are green")

elif userIn == "Green":
    print ("Trees are green")

elif userIn == "blue":
    print ("The sky is blue")

elif userIn == "Blue":
    print ("The sky is blue")

elif userIn == "red":
    print ("Blood is red")

elif userIn == "Red":
    print ("Blood is red")

elif userIn == "yellow":
    print ("Sunflowers are yellow")

elif userIn == "Yellow":
    print ("Sunflowers are yellow")

else:
    print ("I only know 4 colors or you cannot spell")
