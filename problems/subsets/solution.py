class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, op):
            if len(nums) == 0:
                res.append(op[:])
                return
            op1 = op
            op2 = op + [nums[0]]
            nums = nums[1:]
            backtrack(nums, op1)
            backtrack(nums, op2)
        
        backtrack(nums, [])
        return list(res)