class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[math.ceil(len(nums)//2)]
        ans = 0
        for n in nums:
            ans += abs(mid - n)
            
        return ans