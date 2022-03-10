class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, majority = 1, nums[0]
        for n in nums[1:]:
            if n == majority:
                count += 1
            else:
                count -= 1
            if count == 0:
                count = 1
                majority = n
        if nums.count(majority) >= (len(nums)//2):
            return majority