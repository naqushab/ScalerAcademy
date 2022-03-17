class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.list.append(val)
            self.hashmap[val] = len(self.list) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            index = self.hashmap[val]
            if index == len(self.list) -1:
                del self.hashmap[val]
                self.list.pop()
            else:
                del self.hashmap[val]
                self.hashmap[self.list[len(self.list)-1]] = index
                self.list[index], self.list[len(self.list)-1] = self.list[len(self.list)-1], self.list[index]
                self.list.pop()
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        randindex = random.randint(0, len(self.list)-1)
        return self.list[randindex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()