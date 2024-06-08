class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max, current = 0, 0

        for altitude in gain:
            current += altitude

            if current > max:
                max= current
        return max

