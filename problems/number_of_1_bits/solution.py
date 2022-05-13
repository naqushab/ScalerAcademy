class Solution:
    def hammingWeight(self, n: int) -> int:
        count_ones = 0
        while n > 0:
            n = n & n-1
            count_ones += 1
        return count_ones