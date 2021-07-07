from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            stone1 = stones[-1]
            stone2 = stones[-2]
            if stone1 != stone2:
                stones[-2] = abs(stone1-stone2)
                stones = stones[:-1]
            else:
                stones = stones[:-2]
        if len(stones) ==1:
            return stones[0]
        else:
            return 0