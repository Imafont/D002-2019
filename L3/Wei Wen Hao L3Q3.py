def words(x):
    l = []
    check = 0
    while check < 10:
        check += 1
        w = input("Enter a word:\n")
        if (w[0].lower() == "a" or w[0].lower() == "e" or w[0].lower() == "i" or w[0].lower() =="o" or w[0].lower() =="u"):
            l.append(w)
        else:
            print('no')
    print(l)
words(1)
