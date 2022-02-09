class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        m = collections.Counter(nums)
        count = 0
        for key,val in m.items():
            if k == 0 and val >= 2:
                count += 1
            elif k!=0 and k+key in m:
                count += 1
        return count