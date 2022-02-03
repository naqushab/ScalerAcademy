from collections import deque


def find_order(tasks, prerequisites):
  sortedOrder = []
  if tasks <= 0:
    return sortedOrder
  indegree = {i: 0 for i in range(tasks)}
  graph = {i: [] for i in range(tasks)}
  for preq in prerequisites:
    parent, child = preq
    graph[parent].append(child)
    indegree[child] += 1
  source = deque()
  for task in indegree:
    if indegree[task] == 0:
      source.append(task)
  while source:
    parent = source.popleft()
    sortedOrder.append(parent)
    for child in graph[parent]:
      indegree[child] -= 1
      if indegree[child] == 0:
        source.append(child)
  
  return sortedOrder


def main():
  print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
