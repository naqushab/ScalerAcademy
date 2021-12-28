class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = Counter(nums)
        return n[target] > len(nums)//2