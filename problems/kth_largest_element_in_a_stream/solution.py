import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.mh = []
        for n in nums[:self.k]:
            heapq.heappush(self.mh, n)
        for n in nums[self.k:]:
            if self.mh[0] < n:
                heapq.heapreplace(self.mh, n)

    def add(self, val: int) -> int:
        if not self.mh:
            heapq.heappush(self.mh, val)
        if len(self.mh) < self.k:
            heapq.heappush(self.mh, val)
        elif self.mh and self.mh[0] <= val:
            heapq.heappushpop(self.mh, val)
        return self.mh[0] if len(self.mh) == self.k else -1


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)