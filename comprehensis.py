
lst = [-2, 3, -5, 8, -1]
positive = [x for x in lst if x > 0]
print(positive)


N = [1, 2, 3, 4]
squares = [x**2 for x in N]
print(squares)



word = "engineering"
vowels = [ch for ch in word if ch.lower() in 'aeiou']
print(vowels)



word = "hello"
ordinals = [ord(ch) for ch in word]
print(ordinals)
