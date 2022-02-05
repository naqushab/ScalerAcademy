from __future__ import print_function
from heapq import *


class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __lt__(self, other):
    return self.value < other.value


def merge_lists(lists):
  # TODO: Write your code here
  ans = dummy = ListNode(-1)
  h = []
  for l in lists:
    if l:
      heappush(h, l)

  while h:
    n = heappop(h)
    ans.next = n
    n_next = n.next
    ans = ans.next
    ans.next = None
    if n_next:
      heappush(h, n_next)
  return dummy.next


def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result != None:
    print(str(result.value) + " ", end='')
    result = result.next


main()

