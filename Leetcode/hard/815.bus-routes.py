#
# @lc app=leetcode id=815 lang=python3
#
# [815] Bus Routes
#
# https://leetcode.com/problems/bus-routes/description/
#
# algorithms
# Hard (45.05%)
# Likes:    1848
# Dislikes: 49
# Total Accepted:    78.1K
# Total Submissions: 173.2K
# Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
#
# You are given an array routes representing bus routes where routes[i] is a
# bus route that the i^th bus repeats forever.
# 
# 
# For example, if routes[0] = [1, 5, 7], this means that the 0^th bus travels
# in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# 
# 
# You will start at the bus stop source (You are not on any bus initially), and
# you want to go to the bus stop target. You can travel between bus stops by
# buses only.
# 
# Return the least number of buses you must take to travel from source to
# target. Return -1 if it is not possible.
# 
# 
# Example 1:
# 
# 
# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then
# take the second bus to the bus stop 6.
# 
# 
# Example 2:
# 
# 
# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target
# = 12
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 10^5
# All the values of routes[i] are unique.
# sum(routes[i].length) <= 10^5
# 0 <= routes[i][j] < 10^6
# 0 <= source, target < 10^6
# 
# 
#

# @lc code=start
import collections
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        bus_map = collections.defaultdict(set)
        for i in range(len(routes)):
            for dest in routes[i]:
                bus_map[dest].add(i)
        
        visited = set()
        q = collections.deque()
        q.append((source, 0))
        visited.add(source)
        while q:
            place, cost = q.popleft()
            if place == target:
                return cost
            for src in bus_map[place]:
                for dest in routes[src]:
                    if dest not in visited:
                        visited.add(dest)
                        q.append([dest, cost+1])
                routes[src] = [] # this line makes sure you don't process this route again.
        return -1

if __name__ == '__main__':
    s = Solution()
    routes = [[1,2,7],[3,6,7]]
    source = 1
    target = 6
    print(s.numBusesToDestination(routes, source, target))
    routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
    source = 15
    target = 12
    print(s.numBusesToDestination(routes, source, target))

# @lc code=end

