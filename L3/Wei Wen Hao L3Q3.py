def words(x):
    l = []
    for i in range(0, 10):
        w = input("%i Enter a word:" %i)
        first = w[0]
        if first in "AEIOUaeiou":
            l.append(w)
    print(l)
words(1)
