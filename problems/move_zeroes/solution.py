class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        p = 0
        while p < len(nums):
            if nums[p] == 0:
                p += 1
            else:
                nums[s], nums[p] = nums[p], nums[s]
                p += 1
                s += 1