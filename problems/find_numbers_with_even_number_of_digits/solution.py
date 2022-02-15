class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            s = str(n)
            if len(s)%2 == 0:
                count += 1
        return count