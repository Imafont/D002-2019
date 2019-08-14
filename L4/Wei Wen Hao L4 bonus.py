print("rectangle(Top left coordinate, bottom right coordinate, second top left coordinate, second bottom right coordinate")
def rectangle(a1, c1, a2, c2):
    if ((a1[0] > c2[0] or a2[0] > c1[0]) or (a1[1] < c2[1] or a2[1] < c1[1])):
        print("The rectangles will not overlap.")
        return
    print("The rectangles will overlap.")
    return


