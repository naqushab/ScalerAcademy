"""
Problem Statement#
Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. The cost of connecting two ropes is equal to the sum of their lengths.
"""

from heapq import heapify, heappop, heappush

def minimum_cost_to_connect_ropes(ropeLengths):
  result = 0
  # TODO: Write your code here
  if len(ropeLengths) <= 1:
    return 0
  heapify(ropeLengths)
  min_cost = 0
  while len(ropeLengths) > 1:
    min_cost = heappop(ropeLengths) + heappop(ropeLengths)
    result += min_cost
    heappush(ropeLengths, min_cost)
  return result


def main():

  print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()

