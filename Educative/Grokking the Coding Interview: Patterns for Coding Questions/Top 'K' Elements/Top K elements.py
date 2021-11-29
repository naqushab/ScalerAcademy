"""
Problem Statement#
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.
"""
from heapq import *


def find_k_largest_numbers(nums, k):
  result = []
  # TODO: Write your code here
  s = []
  if k >= len(nums):
    return nums
  else:
    for n in nums:
      heappush(s, n*-1)
    for i in range(k):
      result.append(s[i]*-1)
  return result

def find_k_largest_numbers_min_heap(nums, k):
  result = []
  # TODO: Write your code here
  s = []
  if k >= len(nums):
    return nums
  else:
    for n in nums[:k]:
      heappush(result, n)
    for n in nums[k:]:
      if n > result[0]:
        heappop(result)
        heappush(result, n)
  return result

def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()

