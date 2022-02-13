import heapq

def solve(A):
    running_sum = 0
    ans = 0
    for n in A:
        running_sum += n
        if running_sum <= 0:
            ans += 1
            running_sum -= n
    return ans

assert solve([5, -50, 5, 5, -50, -1, -1, -5, -3, 100]) == 2
assert solve([10, -10, -1, -1, 10]) == 1
assert solve([-1, -1, -1, 1, 1, 1, 1]) == 3
assert solve([5, -2 -3, 1]) == 0