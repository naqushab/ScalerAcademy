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