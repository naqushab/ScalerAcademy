class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        import heapq
        min_heap, max_heap = [], []
        for n in C:
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)

        min_cost, max_cost = 0, 0
        while A > 0:
            min_cost_val = heapq.heappop(min_heap)
            min_cost += min_cost_val
            min_cost_val -= 1
            if min_cost_val > 0:
                heapq.heappush(min_heap, min_cost_val)
            max_cost_val = -heapq.heappop(max_heap)
            max_cost += max_cost_val
            max_cost_val -= 1
            if max_cost_val > 0:
                heapq.heappush(max_heap, -max_cost_val)
            A -= 1
        return [max_cost, min_cost]

if __name__ == "__main__":
    print(Solution().solve(4, 3, [2, 1, 1]))