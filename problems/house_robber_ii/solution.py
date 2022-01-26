class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)
        @functools.cache
        def dp(nums):
            if len(nums) == 0:
                return 0
            return max(nums[0]+dp(nums[2:]), dp(nums[1:]))
        
        return max(dp(tuple(nums[1:])), dp(tuple(nums[:-1])))