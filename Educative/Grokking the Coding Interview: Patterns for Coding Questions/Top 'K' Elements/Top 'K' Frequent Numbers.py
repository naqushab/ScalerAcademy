"""
Problem Statement#
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

"""
from heapq import heappop, heappush

def find_k_frequent_numbers(nums, k):
  topNumbers = []
  # TODO: Write your code here
  freq = {}
  for n in nums:
    if n not in freq:
      freq[n] = 0
    freq[n] += 1
  min_heap = []
  for n, f in freq.items():
    heappush(min_heap, (n,f))
    if len(min_heap) > k:
      heappop(min_heap)
  for v in min_heap:
    topNumbers.append(v[1])
  return topNumbers


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()

