class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = 1
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        prev = 1
        for i in range(n-1, -1, -1):
            ans[i] = prev * ans[i]
            prev *= nums[i]
        return ans