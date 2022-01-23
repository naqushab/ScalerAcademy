class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        p, n = 0, 1
        ans = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                ans[p] = nums[i]
                p += 2
            else:
                ans[n] = nums[i]
                n += 2
        return ans