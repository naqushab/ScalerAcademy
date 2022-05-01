import collections

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.dic = {}
        self.dq = collections.deque([])
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if key not in self.dic:
            return -1
        self.dq.remove(key)
        self.dq.append(key)
        return self.dic[key]

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.dic:
            self.dq.remove(key)
        elif len(self.dic) == self.capacity:
            v = self.dq.popleft()
            self.dic.pop(v)
        self.dq.append(key)
        self.dic[key] = value
