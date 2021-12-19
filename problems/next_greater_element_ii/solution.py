from collections import deque

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        filled = [False]*len(nums)
        s = deque()
        for i in range(len(nums)-1, -1, -1):
            while s and s[-1] <= nums[i]:
                s.pop()
            if s:
                ans[i] = s[-1]
                filled[i] = True
            s.append(nums[i])
        for i in range(len(nums)-1, -1, -1):
            if not filled[i]:
                while s and s[-1] <= nums[i]:
                    s.pop()
                if s:
                    ans[i] = s[-1]
                    filled[i] = True
        return ans
        