print("To start the function type factor(number).")
def factor(n):
    for x in range(1, n+1):
        if n%x == 0:
            print("%d divides %d" % (x, n))
