class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res  = []
        
        def backtrack(start, op):
            if len(op) == k:
                res.append(op[:])
            for i in range(start, n+1):
                op.append(i)
                backtrack(i+1, op)
                op.pop()
            
        backtrack(1, [])
        return res