class Rectangle:
    def __init__(self, length, width):
      self.__length = length # private attribute
      self.__width = width # private attribute
    def area(self):
      return self.__length * self.__width
# Overload &lt; operator to compare areas
    def __lt__(self, other):
      return self.area() < other.area()

# Read values from keyboard for first rectangle
l1 = float(input("Enter length of Rectangle 1: "))
w1 = float(input("Enter width of Rectangle 1: "))
r1 = Rectangle(l1, w1)
# Read values from keyboard for second rectangle
l2 = float(input("Enter length of Rectangle 2: "))
w2 = float(input("Enter width of Rectangle 2: "))
r2 = Rectangle(l2, w2)
# Compare using overloaded &lt; operator
if r1 < r2:
    print("Rectangle 1 has smaller area than Rectangle 2 ")
else:
    print("Rectangle 1 has greater or equal area than Rectangle 2 ")
