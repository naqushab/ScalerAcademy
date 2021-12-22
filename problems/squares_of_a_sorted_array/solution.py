class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pivot = 0
        nums = [x*x for x in nums]
        ans = [-1]*len(nums)
        while pivot < len(nums)-1:
            if nums[pivot] < nums[pivot+1]:
                break
            pivot += 1
        ans_iterator = 0
        neg_iterator = pivot -1
        while neg_iterator >= 0 and pivot < len(nums):
            if nums[pivot] < nums[neg_iterator]:
                ans[ans_iterator] = nums[pivot]
                ans_iterator += 1
                pivot += 1
            elif nums[pivot] >= nums[neg_iterator]:
                ans[ans_iterator] = nums[neg_iterator]
                ans_iterator += 1
                neg_iterator -= 1
        while pivot < len(nums):
            ans[ans_iterator] = nums[pivot]
            ans_iterator += 1
            pivot += 1
        while neg_iterator >= 0:
            ans[ans_iterator] = nums[neg_iterator]
            ans_iterator += 1
            neg_iterator -= 1
        return ans