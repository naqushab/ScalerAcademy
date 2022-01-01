class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        not_used = [True]*n
        
        def backtrack(nums, perm):
            if len(perm) == n:
                ans.append(perm[:])
                return
            for i in range(len(nums)):
                if not_used[i]:
                    not_used[i] = False
                    perm.append(nums[i])
                    backtrack(nums, perm)
                    not_used[i] = True
                    perm.pop()
            
            
        backtrack(nums, [])
        return ans
        