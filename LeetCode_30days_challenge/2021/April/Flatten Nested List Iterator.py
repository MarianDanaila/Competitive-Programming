# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
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
        self.flatten = []
        stack = [nestedList]
        while stack:
            curr = stack.pop()
            if isinstance(curr, NestedInteger):
                integer = curr.getInteger()
                lst = curr.getList()
                if integer is not None:
                    self.flatten.append(integer)
                else:
                    stack.append(lst)
            else:
                for el in curr:
                    stack.append(el)
        self.index = len(self.flatten)

    def next(self) -> int:
        self.index -= 1
        return self.flatten[self.index]

    def hasNext(self) -> bool:
        return self.index > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
