class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return sum(cost)
        cost.sort(reverse=True)
        i = 0
        ans = 0
        while i < len(cost):
            if i%3!=2:
                ans += cost[i]
            i+=1
        return ans