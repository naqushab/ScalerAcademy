class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res= set()
        n = len(s)
        
        def backtrack(s, op):
            if len(op) == n:
                res.add(''.join(op))
                return
            op1 = op + [s[0].lower()]
            op2 = op + [s[0].upper()]
            s = s[1:]
            backtrack(s, op1)
            backtrack(s, op2)
        
        backtrack(list(s.lower()), [])
        return list(res)