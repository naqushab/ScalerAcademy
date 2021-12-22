class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i, n in enumerate(nums2):
                nums1[i] = n
            return
        e = m+n-1
        pe = m-1
        i = m
        while pe >=0 and i > 0:
            nums1[e], nums1[pe] = nums1[pe], nums1[e]
            e -= 1
            pe -= 1
            i -= 1
        n1_i = (m+n)-m
        n2_i = 0
        i = 0
        while n2_i < n and n1_i<m+n and i <= m+n-1:
            if nums1[n1_i] < nums2[n2_i]:
                nums1[i] = nums1[n1_i]
                n1_i += 1
                i += 1
            elif nums1[n1_i] >= nums2[n2_i]:
                nums1[i] = nums2[n2_i]
                n2_i += 1
                i += 1
        while n2_i < n:
            nums1[i] = nums2[n2_i]
            i += 1
            n2_i += 1
        