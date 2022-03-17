class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l <= r:
            m = (l+r)//2
            if self.sum_feasible(nums, threshold, m):
                ans = m
                r = m-1
            else:
                l = m+1
        return ans
    
    def sum_feasible(self, nums, threshold, m):
        total_sum = 0
        for i in range(len(nums)):
            total_sum += math.ceil(nums[i]/m)
        return total_sum <= threshold