vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
s = input("Enter the string: ")
vowel_list = []
for ch in s:
    if ch in vowels:
        vowel_list.append(ch)
print("Vowels in the given string are: ", vowel_list)
