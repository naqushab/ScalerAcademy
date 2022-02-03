class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        m = collections.defaultdict(lambda : 0)
        for n3 in nums3:
            for n4 in nums4:
                m[n3+n4] += 1
                
        count = 0
        
        for n1 in nums1:
            for n2 in nums2:
                if -(n1+n2) in m:
                    count += m[-(n1+n2)]
        
        return count