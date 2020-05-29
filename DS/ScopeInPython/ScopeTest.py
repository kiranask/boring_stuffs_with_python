class Difference:
    def __init__(self, a):
        self.__elements = a


    def computeDifference(self):
        self.max_value = max(self.__elements)

        self.min_value = min(self.__elements)

    def maximumDifference(self):

        return abs(self.max_value - self.min_value)





t = Difference([100,2])
t.computeDifference()
print(t.maximumDifference())
# _ = input()
# a = [int(e) for e in input().split(' ')]
# print(a)
# d = Difference([100, 2])
# d.computeDifference()
    # print(d.te)