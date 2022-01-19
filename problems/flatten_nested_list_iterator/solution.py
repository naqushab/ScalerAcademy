# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.it = []
        self.pos = -1
        def flatten(nestedList):
            for item in nestedList:
                if item.isInteger():
                    self.it.append(item.getInteger())
                else:
                    flatten(item.getList())
        flatten(nestedList)
    
    def next(self) -> int:
        self.pos += 1
        return self.it[self.pos]
    
    def hasNext(self) -> bool:
        return self.pos + 1 < len(self.it)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())