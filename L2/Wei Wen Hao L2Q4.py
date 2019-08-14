def math_problem(x):
    print("To find the answer to the question a + b + c + d = 60, ab + bc + cd, we must first prove some things.")
    print("Looking at the second equation we immediately notice that b and c appear more frequently throughout, while a and d less so. Thus we can make the assumption that b and c should be larger then a and d.")
    print("Thus for our first move, we will make both b = c = 1. This gives us a + 1 + 1 + d = 60 or a + d = 58, and 1 x a + 1 x 1 + 1 x d or a + d + 1.")
    print("This tells us that when b and c are constant, it doesn't matter what a and d are.")
    print("Next, let's switch it up and instead make a = d = 1. This gives us 1 + b + c + 1 = 60 or b + c = 58, and 1 x b + bc + 1 x d or b + c + bc.")
    print("Now we can use a program to find out which distribution of values gives us the largest result.")
    b = 1
    x = int(input("Enter any integer:\n"))
    while b < x:
        c = x - b
        answer = b + c + b*c
        print("When b = %d and c = %d, b + c + b*c = %d" %(b, c , answer))
        b = b + 1

    print("From this, we can see we get the largest value when b == c.")
    print("Therefore we know we get the largest value when b == c, and when b == c, it doesn't matter what a and d are.")
    print("Therefore we can change: a + b + c + d = 60 to 2a + 2b = 60 or a + b = 30.")
    print("Our new equation will now be: a + b = 30 and b**2 + 2ab, we can now use a program to find the largest number we can get from this equation.")
    b = 1
    while b <= 30:
        a = 30 - b
        answer_two = b**2 + 2*a*b
        print("When a = %d and b = %d, b**2 + 2*a*b = %d" %(a, b, answer_two))
        b = b + 1

    print("Therefore when a + b + c + d = 60, the largest number we can get from ab + bc + cd is 900. (a = d = 0, b = c = 30)")


math_problem(1)  
