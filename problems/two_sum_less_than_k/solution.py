class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) <=1:
            return -1
        nums.sort()
        l, r = 0, len(nums)-1
        ans = -1
        while l < r:
            s = nums[l] + nums[r]
            if s < k:
                ans = max(ans, s)
                l += 1
            else:
                r -= 1
        return ans