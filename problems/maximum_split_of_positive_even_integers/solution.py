class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2 != 0:
            return []
        ans = []
        sub = 2
        while finalSum >= sub:
            ans.append(sub)
            finalSum -= sub
            sub += 2
        if finalSum > 0:
            ans[-1] = ans[-1] + finalSum
        return ans