# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m + n)

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # First, turn the knowledge array into a dictionary
        knowledge = {key: value for key, value in knowledge}

        # Then, iterate the string
        evaluated, key, is_key = [], [], False
        for c in s:
            # If we find an open parenthesis, start populating the key
            if c == "(":
                is_key = True
                continue
            
            # If we find a closed one instead
            if c == ")":
                # Stop populating the key
                is_key = False

                # Evaluate the current key
                string, key = "".join(key), []
                value = knowledge[string] if string in knowledge else "?"

                # And add it to the final evaluated string
                evaluated += value
                continue
            
            # Otherwise, either populate final evaluated string or current key
            if is_key:
                key.append(c)
            else:
                evaluated.append(c)
        
        # Finally, return the fully evaluated key
        return "".join(evaluated)
