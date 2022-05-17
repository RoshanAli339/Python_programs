string = input('Enter a string: ').strip()
sub = input("Enter a substring: ").strip()

count = 0
for i in range(0, len(string)):
    if string[i:].startswith(sub):
        count += 1
    
print("The count of sub string is: ", count)