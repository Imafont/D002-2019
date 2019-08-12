from math import *

people = int(input("How many people are sharing the bill?\n"))
bill = float(input("How much is the bill?\n"))
print("Kevin paid the bill first. But Kevin only has 100 dollar notes")
x = ceil(bill/100)*100
y = x - bill
z = bill/people

print("So Kevin is going to pay $%d." % (x))
print("The cafe is giving %f to Kevin." % (y))
print("Each one should give %f to Kevin." % (z))

number = 1
while number <= 100:
    if (number%7 == 0 or number%10 == 7):
        print 'X',
    else:
        print number,    
    number = number + 1
print("\nGame Over.")

from random import randint

count = 0
while number != 6:
    number = randint(1, 6)
    print("I got a %d" % number)
    count = count + 1

print("Oh, it takes me %d times to get a 6!!!" % count)
tab = 0
count = 0
while tab <= 100:
    tab = tab + 1
    number = 0
    while number != 6:
        number = randint(1, 6)
        count = count + 1
print('It takes an average of %f times to get a 6 from rolling a dice a 100 times.' % (count/100))
        
