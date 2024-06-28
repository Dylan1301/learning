# Leetcode: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        buy = [0] * 101
        total, free, current = 0, 0, 0
        for i in cost:
            buy[i] += 1
        for index in range(len(buy)-1, 0, -1):
            while buy[index] != 0:
                if free > 0:
                    buy[index] -= 1
                    free -= 1
                    continue

                if current == 2:
                    free +=1
                    current = 0
                    continue

                total += index
                buy[index] -=1
                current +=1
        return total

