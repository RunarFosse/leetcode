# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minLength(self, s: str) -> int:
        # Using doubly linked list
        class Node:
            def __init__(self, char: str, last: "Node"):
                self.char = char
                self.last = last
                self.next = None
        
        # Turn the string into a doubly linked list
        current, length = None, 0
        for c in s:
            # Create a linked list node, and connect it 
            node = Node(c, current)
            if not current:
                current = node
                length += 1
                continue
            current.next = Node
            
            # Check if these two make a valid substring, if so, delete both
            substring = current.char + node.char
            if substring in ["AB", "CD"]:
                current = current.last
                length -= 1
                continue
            
            # If not, add to length and set node to current
            current = node
            length += 1
        
        # At last, return the length of the remaining string
        return length