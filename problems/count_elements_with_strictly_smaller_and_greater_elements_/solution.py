class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        nums.sort()
        f = nums[0]
        l = nums[-1]
        c = 0
        for x in nums:
            if x!=f and x!=l:
                c+=1
        return c