n = int(input("Enter a Number: "))
def sum_of_digit(n):
    s = 0
    n = abs(n)
    while n > 0:
        s += n % 10
        n = n // 10
    return s
print(sum_of_digit(n))
