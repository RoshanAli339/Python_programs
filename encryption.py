def rotate_word(str, rotation):
    new = ''
    for i in range(0, len(str)):
        if ord(str[i]) + rotation > 122:
            ele = chr( (ord(str[i]) + rotation - 122) + 97)
            print(ele)
        elif ord(str[i]) + rotation < 97:
            ele = chr( 122 - (97 - ord(str[i]) + rotation))
            print(ele)
        else:
            ele = chr(ord(str[i]) + rotation)
            print(ele)
        new = new + ele
  
    return new


word = input('Enter any word: ')
x = int(input('Enter the value of rotation: '))
print(f'The encryption of {word} is: ', rotate_word(word, x))