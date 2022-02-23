class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod, suffix_prod = [1]*n, [1]*n
        for i in range(n):
            s = n-i-1
            if i == 0:
                prefix_prod[i] = nums[i]
                suffix_prod[s] = nums[s]
            else:
                prefix_prod[i] = prefix_prod[i-1] * nums[i]
                suffix_prod[s] = suffix_prod[s+1] * nums[s]
        ans = [1]*n
        for i in range(n):
            if i == 0:
                ans[i] = suffix_prod[i+1]
            elif i == n-1:
                ans[i] = prefix_prod[i-1]
            else:
                ans[i] = prefix_prod[i-1] * suffix_prod[i+1]
        return ans
                
        