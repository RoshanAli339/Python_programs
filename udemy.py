def myfunc(sen):
    sen2 = ''
    i = 1
    for c in sen:
        if i % 2 == 0:
            sen2 += c.lower()
        else:
            sen2 += c.upper()
        i += 1
    return sen2


word = input("Enter a word: ")
print(myfunc(word))
