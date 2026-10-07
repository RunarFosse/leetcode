# Author: Runar Fosse
# Time complexity: O(n^22^n)
# Space complexity: O(n2^n)

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Using BFS

        # Initialize the queue with the current string, and perform BFS
        queue, seen, valids = deque([s]), set(), []
        while queue:
            # Get the next unseen string in the queue
            string = queue.popleft()
            if string in seen:
                continue
            seen.add(string)

            # Check if this string is valid
            difference = 0
            for c in string:
                if c in "()":
                    difference += 1 if c == "(" else -1

                if difference < 0:
                    break
            
            # If it is, add to valid and continue
            if difference == 0:
                valids.append(string)
                continue
            
            # If not, and we've found other valid strings with less removals
            if valids and len(valids[0]) > len(string):
                # Then stop, as we've exceeded the minimum number of removals
                break
            
            # Otherwise, remove any parenthesis character and add back into queue
            prefix, suffix = [], deque(string)
            while suffix:
                c = suffix.popleft()
                if c in "()":
                    new_string = "".join(prefix + list(suffix))
                    queue.append(new_string)
                prefix.append(c)
        
        # Finally, return all resulting valid strings
        return valids
