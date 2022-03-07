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
                routes[src] = []
        return -1
'''
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
'''