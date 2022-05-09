class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        if not nums:
            return 0
        l = 0
        for i in range(len(self.nums)):
            l = max(l, self.top_down_ideal(i))
        return l
            
    @functools.lru_cache(None)
    def top_down_ideal(self, index):
        if index >= len(self.nums):
            return 0
        ans = 1
        for next in range(index+1, len(self.nums)):
            if self.nums[next] > self.nums[index]:
                ans = max(ans, 1 + self.top_down_ideal(next))
        return ans
    
    @functools.lru_cache(None)
    def top_down(self, prev, cur):
        if cur == len(self.nums):
            return 0
        op1 = 0
        if prev == -1 or self.nums[prev] < self.nums[cur]:
            op1 = 1 + self.top_down(cur, cur+1)
        op2 = self.top_down(prev, cur+1)
        return max(op1, op2)
        
    
    def bottom_up(self, nums):
        lis = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], lis[j]+1)
                    
        return max(lis)