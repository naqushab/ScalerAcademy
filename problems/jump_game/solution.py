class Solution:
    @lru_cache(None)
    def can_jump(self, nums):
        if not nums:
            return True
        hops = nums[0]
        if len(nums) == 1 and hops == 0:
            return True
        if hops == 0:
            return False
        return any(self.can_jump(nums[hop:]) for hop in range(1, hops+1) if hop <= len(nums))
        
    
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0