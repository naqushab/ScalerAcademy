class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        while l<=r:
            mid = (l+r)//2
            if self.feasible(nums, m, mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
    
    def feasible(self, nums, m, mid):
        total_sum = 0
        splits = 1
        for i in range(len(nums)):
            if total_sum + nums[i] <= mid:
                total_sum += nums[i]
            elif splits < m:
                total_sum = nums[i]
                splits += 1
            else:
                return False
        return True