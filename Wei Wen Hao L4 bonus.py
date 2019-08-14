def rectangle(a1, c1, a2, c2):
    ul = [min(a1[0], c1[0])] + [max(a1[1], c1[1])]
    br = [max(a1[0], c1[0])] + [min(a1[1], c1[1])]
    ul2 = [min(a2[0], c2[0])] + [max(a2[1], c2[1])]
    br2 = [max(a2[0], c2[0])] + [min(a2[1], c2[1])]
    if ((ul[0] > br2[0] or ul2[0] > br[0]) or (ul[1] < br2[1] or ul2[1] < br[1])):
        print("The rectangles will not overlap.")
        return
    print("The rectangles will overlap.")
    return


