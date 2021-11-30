"""
Problem Statement#
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

"""

from heapq import heappop, heappush

def find_Kth_smallest_number(nums, k):
  # TODO: Write your code here
  res = []
  for n in nums[:k]:
    heappush(res, -n)
  for n in nums[k:]:
    if -n > res[0]:
      heappop(res)
      heappush(res, -n)
  return -res[0]


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
