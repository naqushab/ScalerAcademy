class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def recurse(candidates, temp, target):
            if target == 0:
                ans.append(temp[:])
                return
            if target < 0:
                return
            for i in range(len(candidates)):
                new_temp = temp + [candidates[i]]
                recurse(candidates[i:], new_temp, target-candidates[i])
        
        recurse(candidates, [], target)
        return list(ans)