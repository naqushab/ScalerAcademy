# # This is the interface that allows for creating nested lists.
# # You should not implement it, or speculate about its implementation
# class NestedInteger:
#     def __init__(self, x):
        
#     # Return true if this NestedInteger holds a single integer, rather than a nested list.
#     def isInteger(self):
        
#     # Return the single integer that this NestedInteger holds, if it holds a single integer
#     # The result is 1e9 if this NestedInteger holds a nested list
#     def getInteger(self):
        
#     # Return the nested list that this NestedInteger holds, if it holds a nested list
#     # The result is an empty list if this NestedInteger holds a single integer
#     def getList(self):
        

class NestedIterator:
    def __init__(self, nestedList):
        self.generator = self.__gen_list(nestedList)
        self.last_value = None

    def __gen_list(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                yield item.getInteger()
            else:
                yield from self.__gen_list(item.getList())
    
    def next(self):
        if not self.hasNext():
            return None
        num, self.last_value = self.last_value, None
        return num
    
    def hasNext(self):
        if self.last_value is not None:
            return True
        try:
            self.last_value = next(self.generator)
            return True
        except:
            return False