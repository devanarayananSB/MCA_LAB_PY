word=input("enter the word")
if word.endswith("ing"):
    word=word[:-3]+"ly"
else:
    word=word+"ing"
print("result:",word)
