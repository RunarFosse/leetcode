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
        self.list = nestedList
        self.nest = None
    
    def next(self) -> int:
        if self.nest and self.nest.hasNext():
            return self.nest.next()
        
        result = self.list.pop(0)

        if result.isInteger():
            return result.getInteger()
        
        self.nest = NestedIterator(result.getList())
        return self.nest.next()
    
    def hasNext(self) -> bool:
        if self.nest and self.nest.hasNext():
            return True

        if not self.list:
            return False

        result = self.list[0]
        if not result.isInteger():
            self.nest = NestedIterator(result.getList())
            if not self.nest.hasNext():
                self.list.pop(0)
                return self.hasNext()
        
        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())