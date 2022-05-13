class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        return len(set(c.values())) == len(list(c.values()))