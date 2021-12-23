class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        for i in range(0, len(nums)+1):
            x ^= i
        for n in nums:
            x ^= n
        return x