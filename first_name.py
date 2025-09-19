names = input("Enter first names separated by space: ").split()
count = sum(name.lower().count('a') for name in names)
print("Occurrences of 'a':", count)
