def is_palindrome(word):
    reverse = word[-1]
    for i in range(len(word)-2, -1, -1):
        reverse += word[i]
    
    print('Reverse= ', reverse)
    if reverse == word:
        return True
    else:
        return False


m = input('Enter the word to check for palindrome: ')
if is_palindrome(m):
    print(f'{m} is a palindrome')
else:
    print(f'{m} is not a palindrome')