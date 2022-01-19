class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return self.val

class LinkedList:
    def __init__(self):
        self.head = None
        self.ll_len = 0

    def __repr__(self):
        n = self.head
        nodes = []
        while n:
            nodes.append(str(n.val))
            n = n.next
        return ' '.join(nodes)

    def __get_node(self, index):
        if index == 0:
            return None, self.head
        else:
            prev = None
            cur = self.head
            while index > 0:
                prev = cur
                cur = cur.next
                index -= 1
            return prev, cur

    def insert_at(self, index, val):
        if index > self.ll_len:
            return
        p, c = self.__get_node(index)
        if not p and not c:
            self.head = ListNode(val)
        else:
            new = ListNode(val)
            if not p:
                new.next = c
                self.head = new
            else:
                temp = p.next
                p.next = new
                new.next = temp
        self.ll_len += 1
    
    def delete_at(self, index):
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

ll = LinkedList()

def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    ll.insert_at(position-1, value)

def delete_node(position):
    # @param position, integer
    # @return an integer
    ll.delete_at(position-1)


def print_ll():
    # Output each element followed by a space
    print(ll.__repr__())