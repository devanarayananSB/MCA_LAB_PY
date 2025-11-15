class Time:
    def __init__(self, h, m):
        self.__h = h
        self.__m = m
    def __add__(self, other):
        total_min = self.__m + other.__m
        total_hr = self.__h + other.__h + total_min // 60
        total_min %= 60
        return Time(total_hr, total_min)
    def show(self):
        print(f"{self.__h} hrs : {self.__m} mins")
t1 = Time(2, 50)
t2 = Time(1, 20)
t3 = t1 + t2
t3.show()
