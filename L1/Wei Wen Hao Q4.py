def leap_year(x):
    print("A leap year is a number that can be evenly divided by 4, but cannot be evenly by 100, unless it is also evenly divided by 400")
    year=int(input("What is the year?\n"))
    if(year%4 == 0 and year%100 != 0):
        print("Yes, %d is a leap year." % year)
    elif(year%400 == 0):
        print("Yes, %d is a leap year." % year)
    else:
        print("No, %d is not a leap year." % year)

leap_year(1)
