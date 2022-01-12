class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max, cur_min = 1, 1
        for n in nums:
            if n == 0:
                cur_max, cur_min = 1, 1
            else:
                tmp_max = cur_max*n
                tmp_min = cur_min*n
                cur_max = max(tmp_max, tmp_min, n)
                cur_min = min(tmp_max, tmp_min, n)
                res = max(cur_max, res)
        return res