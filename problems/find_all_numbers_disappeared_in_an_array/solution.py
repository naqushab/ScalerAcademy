class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m = {}
        for i in range(1, len(nums)+1):
            m[i] = 1
        for n in nums:
            if n in m:
                del m[n]
        ans = []
        for k in m:
            ans.append(k)
        return ans