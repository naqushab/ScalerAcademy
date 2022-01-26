class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n > 1:
            l = self.sortArray(nums[:n//2])
            r = self.sortArray(nums[n//2:])
            nums = self.merge(l, r)
        return nums
    
    def merge(self, l, r):
        ans = []
        while l and r:
            if l[0] <= r[0]:
                ans.append(l.pop(0))
            else:
                ans.append(r.pop(0))
        if l:
            ans.extend(l)
        if r:
            ans.extend(r)
        return ans