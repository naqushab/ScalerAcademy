class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  # TODO: Write your code here
  mid, f = head, head
  while f and f.next:
    mid = mid.next
    f = f.next.next
  prev = mid
  cur = prev.next
  while cur:
    temp = cur.next
    cur.next = prev
    prev = cur
    cur = temp
  l, r = head, prev
  while l != mid:
    if l.value != r.value:
      return False
    l = l.next
    r = r.next
  return True



def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()

