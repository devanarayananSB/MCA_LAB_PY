limit = int(input("Enter the Limit: "))

for i in range(1, limit + 1): 
    for j in range(i):
        print("*", end='')
    print()
