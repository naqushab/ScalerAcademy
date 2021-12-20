class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c_neg = 0
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                c_neg += 1
        if c_neg % 2 == 0:
            return 1
        else:
            return -1