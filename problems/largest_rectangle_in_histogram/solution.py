class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_small = [0]*n
        right_small = [0]*n
        
        left = collections.deque()
        for i in range(n):
            while len(left) > 0 and heights[left[-1]] >= heights[i]:
                left.pop()
            if len(left) > 0:
                left_small[i] = left[-1] + 1
            else:
                left_small[i] = 0
            left.append(i)
        
        right = collections.deque()
        for i in range(n-1, -1, -1):
            while len(right) > 0 and heights[right[-1]] >= heights[i]:
                right.pop()
            if len(right) > 0:
                right_small[i] = right[-1] - 1
            else:
                right_small[i] = n-1
            right.append(i)
        
        ans = 0
        for i in range(n):
            ans = max(ans, (right_small[i]-left_small[i]+1)*heights[i])
        return ans