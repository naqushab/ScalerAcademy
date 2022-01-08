class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod, suffix_prod = [1]*len(nums), [1]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix_prod[i] = nums[i]
            else:
                prefix_prod[i] = prefix_prod[i-1]*nums[i]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffix_prod[i] = nums[i]
            else:
                suffix_prod[i] = nums[i]*suffix_prod[i+1]
        ans = [1]*len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                ans[i] = suffix_prod[i+1]
            elif i == len(nums)-1:
                ans[i] = prefix_prod[i-1]
            else:
                ans[i] = prefix_prod[i-1]*suffix_prod[i+1]
        return ans