class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 2:
            return 0
        left_max, right_max = height[0], height[-1]
        left, right = 1, n-2
        ans = 0
        while left <= right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if left_max < right_max:
                ans += (left_max - height[left])
                left += 1
            else:
                ans += (right_max - height[right])
                right -= 1
        return ans