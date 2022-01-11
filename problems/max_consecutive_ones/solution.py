class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        local_len = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                local_len +=1
            else:
                local_len = 0
            max_len = max(max_len, local_len)
        return max_len