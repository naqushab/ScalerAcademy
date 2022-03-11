#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (37.54%)
# Likes:    10138
# Dislikes: 587
# Total Accepted:    932.5K
# Total Submissions: 2.5M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.
# 
# Return true if you can reach the last index, or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def can_jump(self, nums):
        if not nums:
            return True
        hops = nums[0]
        if hops == 0:
            return False
        return any(self.can_jump(nums[hop:]) for hop in range(1, hops+1) if hop <= len(nums))
    
    def canJump(self, nums: List[int]) -> bool:
        return self.can_jump(nums)

if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2,0,2,0,4]))
    print(s.canJump([3,2,1,0,4]))
# @lc code=end

