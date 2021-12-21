class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m, lm = float('-inf'), 0
        for n in nums:
            lm = max(n, lm + n)
            m = max(m, lm)
        return m