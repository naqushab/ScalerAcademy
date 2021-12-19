from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = deque()
        d = {}
        i = len(nums2)-1
        while i >= 0:
            if not s:
                d[nums2[i]] = -1
            elif s and nums2[i] <= s[-1]:
                    d[nums2[i]] = s[-1]
            elif s and nums2[i] > s[-1]:
                while s and nums2[i] > s[-1]:
                    s.pop()
                if s:
                    d[nums2[i]] = s[-1]
                else:
                    d[nums2[i]] = -1
            s.append(nums2[i])
            i -= 1
        ans = []
        for n in nums1:
            ans.append(d[n])
        return ans