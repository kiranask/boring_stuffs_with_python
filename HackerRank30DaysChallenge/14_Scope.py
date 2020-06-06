class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        self.max_value = max(self.__elements)
        self.min_value = min(self.__elements)
        self.maximumDifference=abs(self.max_value - self.min_value)
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)