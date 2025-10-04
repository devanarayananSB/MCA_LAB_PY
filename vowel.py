vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
s = input("Enter the String: ")
count = 0
for i in range(len(s)):
    if s[i] in vow:
        count += 1
print("The Number of Vowels is:", count)
