class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        l, r = 0, 0
        q = collections.deque()
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()
            if (r+1) >= k:
                ans.append(nums[q[0]])
                l += 1
            r += 1
        return ans