from collections import deque

def print_backtracking(source, graph, indegree, sortedOrder):
  if source:
    for vertex in source:
      sortedOrder.append(vertex)
      source_next = deque(source)
      source_next.remove(vertex)
      for child in graph[vertex]:
        indegree[child] -= 1
        if indegree[child] == 0:
          source_next.append(child)
      print_backtracking(source_next, graph, indegree, sortedOrder)
      sortedOrder.remove(vertex)
      for child in graph[vertex]:
        indegree[child] += 1
  if len(sortedOrder) == len(indegree):
    print(sortedOrder)

def print_orders(tasks, prerequisites):
  sortedOrder = []
  if tasks <= 0:
    return
  indegree = {i: 0 for i in range(tasks)}
  graph = {i: [] for i in range(tasks)}
  for preq in prerequisites:
    parent, child = preq
    graph[parent].append(child)
    indegree[child] += 1
  source = deque()
  for v in indegree:
    if indegree[v] == 0:
      source.append(v)
  print_backtracking(source, graph, indegree, sortedOrder)

def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
