# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        values = { "I" : 1,
                   "V" : 5,
                   "X" : 10,
                   "L" : 50,
                   "C" : 100,
                   "D" : 500,
                   "M" : 1000 }
        
        number = current = 0
        last_value = 0
        # Iterate string, applying roman to integer rules
        for c in s:
            value = values[c]
            
            # Smaller came before -> Apply rule
            if value > last_value:
                current = value - current
                last_value = value
            # Equal came before -> Keep cumulating current
            elif value == last_value:
                current += value
            # Bigger came before -> Add current and recumulate
            else:
                number += current
                current = value
                last_value = value
        
        return number + current
