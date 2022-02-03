from collections import deque

def topological_sort(vertices, edges):
  sortedOrder = []
  # TODO: Write your code here
  if vertices <= 0:
    return sortedOrder
  indegree = {i: 0 for i in range(vertices)}
  graph = {i: [] for i in range(vertices)}
  for path in edges:
    parent, child = path[0], path[1]
    graph[parent].append(child)
    indegree[child] += 1
  source = deque()
  for vertex in graph:
    if len(graph[vertex]) == 0:
      source.append(vertex)
  while source:
    parent = source.popleft()
    sortedOrder.append(parent)
    for child in graph[parent]:
      indegree[child] -= 1
      if indegree[child] == 0:
        source.append(child)
  if len(sortedOrder) != vertices:
    return []
  return sortedOrder


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()