def checker(sentence, letter):
    result = []
    for i in range(0, int(len(sentence)-1)):
        if letter.lower() in sentence[i].lower():
            result.append(i)
    return result