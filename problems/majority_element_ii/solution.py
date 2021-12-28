class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return list(set(nums))
        a = None
        b = None
        ac, bc = 0, 0
        for n in nums:
            if n == a:
                ac += 1
            elif n == b:
                bc += 1
                b = n
            elif ac == 0:
                a = n
                ac = 1
            elif bc == 0:
                b = n
                bc = 1
            else:
                ac -= 1
                bc -= 1
        ans = []
        ac, bc = 0, 0
        for n in nums:
            if n == a:
                ac += 1
            if n == b:
                bc += 1
        if ac > len(nums)//3:
            ans.append(a)
        if bc > len(nums)//3:
            ans.append(b)
        return ans if a!=b else [a]