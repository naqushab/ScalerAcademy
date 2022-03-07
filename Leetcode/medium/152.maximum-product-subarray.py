#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (34.43%)
# Likes:    10659
# Dislikes: 332
# Total Accepted:    690.9K
# Total Submissions: 2M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find a contiguous non-empty subarray within the
# array that has the largest product, and return the product.
# 
# The test cases are generated so that the answer will fit in a 32-bit
# integer.
# 
# A subarray is a contiguous subsequence of the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        n = len(nums)
        cur_product = 1
        min_product, max_product = 1, 1
        for i in range(n):
            if nums[i] == 0:
                min_product = max_product = 0
            else:
                min_prod = min(min_product * nums[i], max_product * nums[i], nums[i])
                max_prod = max(min_product * nums[i], max_product * nums[i], nums[i])
                min_product, max_product = min_prod, max_prod
                ans = max(ans, min_product, max_product)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([-2,1, 4, -1,6, 0,4]))
    print(s.maxProduct([2,3,-2,4]))
# @lc code=end

