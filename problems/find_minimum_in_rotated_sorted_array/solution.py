class Solution:
    def findMin(self, nums: List[int]) -> int:
        s, e = 0, len(nums)-1
        ans = float('inf')
        while s<=e:
            m = (s+e)//2
            if nums[s] <= nums[m]:
                ans = min(ans, nums[s])
                s = m+1
            else:
                ans = min(ans, nums[m])
                e = m-1
        return ans