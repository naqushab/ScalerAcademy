# Definition for singly-linked list.

class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list
    def solve(self, A):
        self.head = None
        self.ll_len = 0

        def add_at_head(val):
            if not self.head:
                self.head = ListNode(val)
            else:
                prev_head = self.head
                self.head = ListNode(val)
                self.head.next = prev_head
            self.ll_len += 1

        def add_at_tail(val):
            if not self.head:
                self.head = ListNode(val)
            else:
                n = self.head
                while n.next:
                    n = n.next
                n.next = ListNode(val)
            self.ll_len += 1
        
        def add_at(val, index):
            if index > self.ll_len:
                return
            else:
                if index == 0:
                    add_at_head(val)
                elif index == self.ll_len:
                    add_at_tail(val)
                else:
                    n = self.head
                    p = None
                    while index > 0:
                        p = n
                        n = n.next
                        index -= 1
                    new = ListNode(val)
                    temp = p.next
                    p.next = new
                    new.next = temp
                    self.ll_len += 1
            
        def delete_at(index):
            if index >= self.ll_len:
                return
            else:
                dummy = prev = ListNode(0)
                prev.next = self.head
                cur = self.head
                while index:
                    prev = cur
                    cur = cur.next
                    index -= 1
                prev.next = cur.next
                self.head = dummy.next
                self.ll_len -= 1

        for op in A:
            operation, val, index = op
            if operation == 0:
                add_at_head(val)
            elif operation == 1:
                add_at_tail(val)
            elif operation == 2:
                add_at(val, index)
            elif operation == 3:
                delete_at(val)
        return self.head

if __name__ == "__main__":
    s = Solution()
    A = [[3, 1, -1], [1, 4, -1], [2, 5, 1], [0, 19, -1], [2, 5, 1], [3, 3, -1], [3, 2, -1], [3, 1, -1], [2, 1, 1], [1, 7, -1], [0, 2, -1], [0, 15, -1]]
    s.solve(A=A)