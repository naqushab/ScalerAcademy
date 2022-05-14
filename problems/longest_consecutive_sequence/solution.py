class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        visited = set()
        l = 1
        for num in s:
            if num in visited:
                continue
            left, right = num, num
            while left in s:
                visited.add(left)
                left -= 1
            else:
                left += 1
            while right in s:
                visited.add(right)
                right += 1
            else:
                right -= 1
            l = max(l, right - left + 1)
        return l