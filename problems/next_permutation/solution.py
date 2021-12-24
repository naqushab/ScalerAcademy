class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        if len(nums) <= 1:
            return nums
        ptr = len(nums) - 2
        while ptr >= 0:
            if nums[ptr] < nums[ptr+1]:
                break
            ptr -= 1
        l = ptr
        if ptr >= 0:
            r = len(nums)-1
            while r > l:
                if nums[l] < nums[r]:
                    break
                r -= 1

            nums[l], nums[r] = nums[r], nums[l]
        reverse(nums, l+1, len(nums)-1)