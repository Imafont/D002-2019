def prime(x):
    number = int(input("Which number do you want to have checked?\n"))
    if number < 2:
        print("Illegal input.")
        return(x)
    n = 2
    while n < number/2:
        if number%n != 0:
            n = n + 1
        else:
            print("%d is not a prime number." % number)
            return(x)
    print("%d is a prime number." % number)

prime(1)
        
