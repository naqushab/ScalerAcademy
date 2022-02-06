class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        o = []
        e = []
        n = len(nums)
        for i in range(n):
            if i%2 == 0:
                e.append(nums[i])
            else:
                o.append(nums[i])
        ans = []
        e.sort()
        o.sort(reverse=True)
        for i in range(n):
            if i%2 == 0:
                ans.append(e.pop(0))
            else:
                ans.append(o.pop(0))
        return ans