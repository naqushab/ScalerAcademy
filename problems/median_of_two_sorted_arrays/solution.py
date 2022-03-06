class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if (m+n) % 2 == 1:
            merged = []
            i, j = 0, 0
            while i < m and j < n and len(merged) <= (m+n)//2:
                if nums1[i] <= nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            while i < m and len(merged) <= ((m+n)//2):
                merged.append(nums1[i])
                i += 1
            while j < n and len(merged) <= ((m+n)//2):
                merged.append(nums2[j])
                j += 1
            return merged[-1]
        else:
            merged = []
            i, j = 0, 0
            while i < m and j < n and len(merged) <= ((m+n)//2):
                if nums1[i] <= nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            while i < m and len(merged) <= ((m+n)//2):
                merged.append(nums1[i])
                i += 1
            while j < n and len(merged) <= ((m+n)//2):
                merged.append(nums2[j])
                j += 1
            return (merged[-1] + merged[-2])/2