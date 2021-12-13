from HashEntry import HashEntry

class HashTable:
    """
    We will use the chaining strategy, 
    along with the resize operation to avoid collisions in the table.
    """
    def __init__(self):
        self.slots = 20
        self.size = 0
        self.buckets = [None] * self.size

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def get_index(self, key):
        hash_val = hash(key)
        index = hash_val % self.slots
        return index

    def resize(self):
        new_slots = self.slots*2
        new_buckets = [None]*new_slots
        for item in self.buckets:
            head = item
            while head:
                new_index = hash(head.key) % new_slots
                if not new_buckets[new_index]:
                    new_buckets[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_buckets[new_index]
                    while node:
                        if node.key == head.key:
                            node.value = head.value
                            node = None
                        elif not node.next:
                            node.next = HashEntry(head.key, head.value)
                            node = None
                        node = node.next
                head = head.next
        self.slots = new_slots
        self.buckets = new_buckets

    def insert(self, key, value):
        b_index = self.get_index(key)
        if not self.buckets[b_index]:
            self.buckets[b_index] = HashEntry(key, value)
            self.size += 1
        else:
            node = self.buckets[b_index]
            while node:
                if node.key == key:
                    node.value = value
                    break
                elif not node.next:
                    node.next = HashEntry(key, value)
                    self.size += 1
                    break
                node = node.next
        if self.size > 0.6*self.slots:
            self.resize()

    def search(self, key):
        b_index = self.get_index(key)
        head = self.buckets[b_index]
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def delete(self, key):
        b_index = self.get_index(key)
        head = self.buckets[b_index]
        if head.key == key:
            self.buckets[b_index] = head.next
            del head
            self.size -= 1
            return
        prev = None
        while head:
            if head.key == key:
                prev.next = head.next
                del head
                self.size -= 1
                return
            prev = head
            head = head.next
        return
