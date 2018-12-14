weekends = {'january' : [6,7,13,14,20,21,27,28],
    'febuary' : [3,4,10,11,17,18,24,25],
    'march' : [3,4,10,11,17,18,24,25,31],
    'april' : [1,7,8,14,15,21,22,28,29],
    'may' : [5,6,12,13,19,20,26,27],
    'june' : [2,3,9,10,16,17,23,24,30],
    'july' : [1,7,8,14,15,21,22,28,29],
    'august' : [4,5,11,12,18,19,25,26],
    'september' : [1,2,8,9,15,16,22,23,29,30],
    'october' : [6,7,13,14,20,21,27,28],
    'november' : [3,4,10,11,17,18,24,25],
    'december' : [1,2,8,9,15,16,22,23,29,30]
            }

d = 1


def asd (monthAndYear) :
    letters = ''
    nums = ''
    for char in monthAndYear :
        try :
            d = int(char)
            nums = nums + char
        except ValueError :
            if char!=' ' :
                letters = letters + char
    return(nums,letters)

def aBunchOfPointlessIfStatements (num, month) :
    a = str(num)
    if month=='january' :
        b = '1'
    elif month=='febuary' :
        b = '2'
    elif month=='march' :
        b = '3'
    elif month=='april' :
        b = '4'
    elif month=='may' :
        b = '5'
    elif month=='june' :
        b = '6'
    elif month=='july' :
        b = '7'
    elif month=='august' :
        b = '8'
    elif month=='september' :
        b = '9'
    elif month=='october' :
        b = '10'
    elif month=='november' :
        b = '11'
    elif month=='december' :
        b = '12'
    c = '2018'
    return (a + '/' + b + '/' + c)
