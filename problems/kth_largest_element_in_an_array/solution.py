class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        n = len(nums)
        for i in range(k):
            heapq.heappush(h, nums[i])
        for i in range(k, n):
            if h[0] < nums[i]:
                heapq.heappop(h)
                heapq.heappush(h, nums[i])
        return h[0]
        