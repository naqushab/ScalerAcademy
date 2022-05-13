class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 1
        for num in nums[1:]:
            if num == majority:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority = num
                count = 1
        
        element_count = 0
        for num in nums:
            if num == majority:
                element_count += 1
        
        return majority if element_count >= len(nums)// 2 else -1