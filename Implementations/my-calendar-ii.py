class MyCalendarTwo:

    def __init__(self):
        # Store singly and doubly booked events in binary search trees
        self.events = Node()
        self.doubles = Node()
        
    def book(self, start: int, end: int) -> bool:
        # Start by calculating overlap with single booked tree
        singly, doubly = self.events.getOverlaps((start, end))

        # Before adding any interval, verify that no
        # interval overlaps with doubly booked tree
        for interval in doubly:
            # If so, we do not add event to booked
            if self.doubles.getOverlaps(interval)[1]:
                return False

        # If there are no overlaps, add all intervals to trees
        for interval in singly:
            self.events.add(interval)
        for interval in doubly:
            self.doubles.add(interval)
        return True

class Node:
    def __init__(self, event: (int, int) = None):
        self.event = event
        self.left = None
        self.right = None
    
    def getOverlaps(self, event: (int, int)) -> ([(int, int)], [(int, int)]):
        # If current event is empty, event does not overlap
        if not self.event:
            return ([event], [])

        # If event does not overlap with current event, recurse
        if event[1] <= self.event[0]:
            return self.left.getOverlaps(event)
        if self.event[1] <= event[0]:
            return self.right.getOverlaps(event)
        
        # If event overlaps, calculate overlapping intervals in left subtree
        singly, doubly = [], []
        if event[0] < self.event[0]:
            interval = (event[0], self.event[0])
            left_singly, left_doubly = self.left.getOverlaps(interval)
            singly += left_singly
            doubly += left_doubly
        
        # Calculate overlap with current event
        interval = (max(event[0], self.event[0]), min(event[1], self.event[1]))
        doubly.append(interval)

        # And calculate overlapping intervals in right subtree
        if self.event[1] < event[1]:
            interval = (self.event[1], event[1])
            right_singly, right_doubly = self.right.getOverlaps(interval)
            singly += right_singly
            doubly += right_doubly
        
        # Finally return intervals
        return (singly, doubly)
    
    def add(self, event: (int, int)) -> None:
        # If node does not contain an event, set to do
        if not self.event:
            self.event = event
            self.left = Node()
            self.right = Node()
            return

        # If not, traverse tree to find correct position
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

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)