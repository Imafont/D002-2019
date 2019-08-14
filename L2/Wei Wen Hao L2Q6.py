import random
def banana_guessing(x):
    count = 0
    print("Welcome to the banna guessing game! Dave hid some bananas, your task is to find out how many. You have 3 chances.")
    n = int(random.randint(1, 100))
    print("shh, Dave hides %d bananas" % n) 
    while count < 3:
        count += 1
        p_guess = int(input("What is your guess?\n"))
        if p_guess == n:
            print("Congratulations! You got the correct guess in %d trial(s)." % count)
            print("Dave's bananas are all yours!")
            return(x)
        else:
            print("Wrong! Try again next time.")
    print("The correct answer is %d. You failed!" % n)

banana_guessing(1)
