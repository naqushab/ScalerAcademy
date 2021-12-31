class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        inc = dc = False
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inc = True
            elif nums[i] > nums[i+1]:
                dc = True
        if inc and dc:
            return False
        else:
            return True