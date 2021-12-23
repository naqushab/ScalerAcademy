class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1, m2 = {}, {}
        for n in nums1:
            if n not in m1:
                m1[n] = 0
            m1[n] += 1
        for n in nums2:
            if n not in m2:
                m2[n] = 0
            m2[n] += 1
        ans = []
        for k in m2.keys():
            if k in m1 and m1[k] > 0 and m2[k] > 0:
                while m1[k] != 0 and m2[k] != 0:
                    ans.append(k)
                    m1[k] -= 1
                    m2[k] -= 1
        return ans