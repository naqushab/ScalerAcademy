class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 1
        m = nums[0]
        for n in nums[1:]:
            if n == m:
                c+=1
            else:
                c-=1
            if c==0:
                m = n
                c = 1
        return m