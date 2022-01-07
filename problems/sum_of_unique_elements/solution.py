class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        ans = 0
        for k, v in c.items():
            if v == 1:
                ans += k
        return ans