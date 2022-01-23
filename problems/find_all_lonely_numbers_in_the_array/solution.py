class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        ans = []
        co = collections.Counter(nums)
        for k,v in co.items():
            if v == 1 and k-1 not in co and k+1 not in co:
                ans.append(k)
        return ans