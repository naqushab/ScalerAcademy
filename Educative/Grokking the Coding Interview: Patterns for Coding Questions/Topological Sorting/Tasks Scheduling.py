from collections import deque

def is_scheduling_possible(tasks, prerequisites):
  # TODO: Write your code here
  if tasks <= 0:
    return True
  indegree = {i: 0 for i in range(tasks)}
  graph = {i: [] for i in range(tasks)}
  for preq in prerequisites:
    parent, child = preq
    graph[parent].append(child)
    indegree[child] += 1
  visited = set()
  source = deque()
  for vertex in indegree:
    if indegree[vertex] == 0:
      source.append(vertex)
  if len(source) == 0:
    return False
  while source:
    parent = source.popleft()
    if parent in visited:
      return False
    else:
      visited.add(parent)
      for child in graph[parent]:
        indegree[child] -= 1
        if indegree[child] == 0:
          source.append(child)
  return True


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
