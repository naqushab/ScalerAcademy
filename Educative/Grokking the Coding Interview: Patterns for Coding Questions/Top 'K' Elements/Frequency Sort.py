"""
Problem Statement#
Given a string, sort it based on the decreasing frequency of its characters.
"""
from heapq import heappush, heappop

def sort_character_by_frequency(str):
  # TODO: Write your code here
  f_m = {}
  for c in str:
    if c not in f_m:
      f_m[c] = 0
    f_m[c] -= 1
  min_heap = []
  for n, f in f_m.items():
    heappush(min_heap, (f, n))
  ans = ""
  while min_heap:
    l, c = heappop(min_heap)
    for i in range(-l):
      ans += c
  return ans


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()
