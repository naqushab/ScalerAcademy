class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0
        while maxDoubles > 0 and target > 1:
            if target % 2 == 0:
                maxDoubles -= 1
                target = target >> 1
                steps += 1
            else:
                target -= 1
                steps += 1
        return steps + (target-1)