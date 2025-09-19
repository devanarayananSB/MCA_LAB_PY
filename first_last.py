s = input("Enter string: ")
if len(s) >= 2:
    swapped = s[-1] + s[1:-1] + s[0]
else:
    swapped = s
print(swapped)
