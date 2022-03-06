class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        right = [0]*n
        prev_gt = 0
        for i in range(n):
            left[i] = prev_gt
            prev_gt = max(height[i], prev_gt)
        prev_gt = 0
        for i in range(n-1, -1, -1):
            right[i] = prev_gt
            prev_gt = max(height[i], prev_gt)
        ans = 0
        for i in range(n):
            water = min(left[i], right[i]) - height[i]
            if water < 0:
                water = 0
            ans += water
        return ans
                