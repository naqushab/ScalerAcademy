class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        m = collections.defaultdict(lambda: 0)
        orig = nums[:]
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                m[nums[i]] = m[nums[i-1]]
            else:
                m[nums[i]] = i
        for i in range(len(orig)):
            ans[i] = m[orig[i]]
        return ans