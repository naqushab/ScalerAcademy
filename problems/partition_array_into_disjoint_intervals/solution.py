class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        max_ltor = [0]*len(nums)
        min_rtol = [0]*len(nums)
        
        max_l = float('-inf')
        for i in range(len(nums)):
            max_l = max(nums[i], max_l)
            max_ltor[i] = max_l
            
        min_r = float('+inf')
        for i in range(len(nums)-1, -1, -1):
            min_r = min(nums[i], min_r)
            min_rtol[i] = min_r
            
        for i in range(len(nums)-1):
            if max_ltor[i] <= min_rtol[i+1]:
                return i+1