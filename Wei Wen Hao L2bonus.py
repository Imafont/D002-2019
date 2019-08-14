import random
def banana_guessing(x):
    count = 0
    print("Welcome to the banna guessing game! Dave hid some bananas, your task is to find out how many.")
    n = int(random.randint(1, 100))
    print("shh, Dave hides %d bananas" % n) 
    while n < 101:
        count += 1
        p_guess = int(input("Player 1, input your guess.\n"))
        if p_guess == n:
            print("Congratulations, player 1 wins! You got the correct guess in %d trial(s)." % count)
            break
        else:
            print("Wrong! Try again next time.")
        p2_guess = int(input("Player 2, input your guess.\n"))
        if p2_guess == n:
            print("Congratulations, player 2 wins! You got the correct guess in %d trial(s)." % count)
            break
        else:
            print("Wrong! Try again next time.")

banana_guessing(1)
