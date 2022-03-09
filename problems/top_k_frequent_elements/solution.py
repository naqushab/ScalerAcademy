class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        h = []
        for n, freq in c.items():
            heapq.heappush(h, (freq, n))
            if len(h) > k:
                heapq.heappop(h)
        ans = []
        for (k, v) in h:
            ans.insert(0, v)
        return ans