class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 1
        ans = nums[0]
        for n in nums[1:]:
            if n == ans:
                c += 1
            else:
                c -= 1
            if c == 0:
                ans = n
                c = 1
        return ans