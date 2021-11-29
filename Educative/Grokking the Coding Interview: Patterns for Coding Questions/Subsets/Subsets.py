"""
Problem Statement#
Given a set with distinct elements, find all of its distinct subsets.
"""

def find_subsets(nums):
  subsets = []
  # TODO: Write your code here
  if not nums:
    return []
  else:
    subsets.append([])
    for n in nums:
      l = len(subsets)
      for i in range(l):
        s = list(subsets[i])
        s.append(n)
        subsets.append(s)
    return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
