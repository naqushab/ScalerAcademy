class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        m = collections.defaultdict(lambda x: -1)
        m[0] = 0
        count = 0
        ans = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count == 0:
                if ans < i+1:
                    ans = i+1
            if count in m:
                ans = max(ans, i - m[count])
            else:
                m[count] = i
        return ans