class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @functools.lru_cache(None)
        def dp(i):
            if i >= len(questions):
                return 0
            return max(dp(i+1), questions[i][0] + dp(i + questions[i][1]+ 1))
        
        return dp(0)