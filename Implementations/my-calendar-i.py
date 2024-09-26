class MyCalendar:
    
    def __init__(self):
        # Store events in a binary search tree
        self.events = None

    def book(self, start: int, end: int) -> bool:
        # If events tree is empty, create it
        if not self.events:
            self.events = Node((start, end))
            return True
        
        # If not, traverse tree and see if any events overlap this
        if self.events.overlaps((start, end)):
            return False
        
        # If not, add event to tree
        self.events.add((start, end))
        return True

class Node:
    def __init__(self, event: (int, int)):
        self.event = event
        self.left = None
        self.right = None
    
    def overlaps(self, event: (int, int)) -> bool:
        # Check if event overlaps with current event
        startOverlap = self.event[0] <= event[0] < self.event[1]
        endOverlap = self.event[0] < event[1] <= self.event[1]
        wholeOverlap = event[0] <= self.event[0] and self.event[1] <= event[1]
        if startOverlap or endOverlap or wholeOverlap:
            return True
        
        # If not, check if overlaps with children
        if event[0] < self.event[0]:
            return self.left.overlaps(event) if self.left else False
        
        if event[0] >= self.event[1]:
            return self.right.overlaps(event) if self.right else False
    
    def add(self, event: (int, int)) -> None:
        # Traverse tree to find correct position
        if event[0] < self.event[0]:
            if not self.left:
                self.left = Node(event)
            else:
                self.left.add(event)
        else:
            if not self.right:
                self.right = Node(event)
            else:
                self.right.add(event)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)