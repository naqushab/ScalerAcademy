class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        import heapq
        h = []
        t = 0
        profit = 0
        time_cost = list(zip(A, B))
        time_cost.sort()
        for i in range(len(time_cost)):
            if t < time_cost[i][0]:
                profit += time_cost[i][1]
                heapq.heappush(h, time_cost[i][1])
                t += 1
            else:
                if time_cost[i][1] > h[0]:
                    profit -= h[0]
                    heapq.heappop(h)
                    heapq.heappush(h, time_cost[i][1])
                    profit += time_cost[i][1]
        return profit % (10**9 + 7)

if __name__ == '__main__':
    A = [ 1, 7, 6, 2, 8, 4, 4, 6, 8, 2 ]
    B = [ 8, 11, 7, 7, 10, 8, 7, 5, 4, 9 ]
    print(Solution().solve(A, B))