class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            if target - n in m:
                return [i, m[target-n]]
            m[n] = i