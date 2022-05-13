class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s, counter_t = collections.Counter(s), collections.Counter(t)
        return counter_s == counter_t