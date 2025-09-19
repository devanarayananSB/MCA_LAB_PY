s = input("Enter string: ")
first_char = s[0]
modified = first_char + s[1:].replace(first_char, '$')
print(modified)
