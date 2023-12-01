# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split path into array, split on "/" char
        path = path.split("/")

        # Store path in a stack
        stack = []
        for directory in path:
            # Directory is empty or is current directory
            if not directory or directory == ".":
                continue
            
            # Go back 1 directory -> pop from stack
            if directory == "..":
                if len(stack) > 0:
                    stack.pop()
                continue
            
            stack.append(directory)
        
        # Join together everything in a stack, with a leading "/"
        return "/" + "/".join(stack)