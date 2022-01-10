class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        m = collections.defaultdict(lambda: 0)
        c = 0
        for n in nums:
            running_sum += n
            if running_sum == k:
                c+=1
            if running_sum-k in m:
                c += m[running_sum-k]
            m[running_sum] += 1
        return c