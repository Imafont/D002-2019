def checker(sentence, letter):
    result = []
    for i in range(0, len(sentence)):
        if letter.lower() in sentence[i].lower():
            result.append(i)
    return result
