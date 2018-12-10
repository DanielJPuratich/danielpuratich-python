from random import randint
def main () :
    times = 0
    cont = 'y'
    while cont=='y' :
        print(thang.genDice(thang(die())))
        times = times + 1
        print ("You have played " + str(times) + " times.")
        cont = input ("Would you like this to run again? (y/n) - ")

def die () :
    w = 'n'
    while w=='n':
        try :
            q = int(input("How many dice do you want to roll? - "))
            if q>0 :
                return (q)
            else :
                print ("This is not a valid number")
        except ValueError:
            print ("This is not a valid number")

class thang :
    def __init__(self, numOfDice):
        self.numOfDice = numOfDice
        self.a = "  ------- " * self.numOfDice
        self.t = ''
        self.u = ''
        self.i = ''
    def genDice (self) :

        for num in range(0 , self.numOfDice) :
            y = randint(1,6)

            if y==1 or y==2 :
                b = ' |       |'
            elif y==3 :
                b = ' |   *   |'
            elif y==4 or y==5 or y==6 :
                b = ' | *  *  |'

            if y==1 or y==3 or y==5 :
                c = ' |   *   |'
            elif y==4 :
                c = ' |       |'
            elif y==2 or y==6 :
                c = ' | *  *  |'

            if y==1 or y==2 :
                d = ' |       |'
            elif y==3 :
                d = ' |   *   |'
            elif y==4 or y==5 or y==6 :
                d = ' | *  *  |'

            self.t = self.t + b
            self.u = self.u + c
            self.i = self.i + d

        return (self.a + "\n" + self.t + "\n" + self.u + "\n" + self.i + "\n" + self.a)

main ()
