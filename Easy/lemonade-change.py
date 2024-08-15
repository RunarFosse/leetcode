# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Store 5 and 10 dollar change received
        fives, tens = 0, 0

        # Iterate each bill
        for bill in bills:
            match bill:
                # If we receive a 5 dollar bill
                case 5:
                    # No need to give out change
                    fives += 1
                
                # If we receive a 10 dollar bill
                case 10:
                    # If we don't have any 5 dollar change, we cannot provide
                    if not fives:
                        return False
                    # Else change in a 5 dollar bill
                    fives -= 1
                    tens += 1
                
                # If we receive a 20 dollar bill
                case 20:
                    # If we have a 5 and 10 dollar bill, hand out change
                    if fives and tens:
                        fives -= 1
                        tens -= 1
                    
                    # If we don't have 10s, but have three 5s, hand out change
                    elif fives >= 3:
                        fives -= 3
                    
                    # If not, we cannot provide
                    else:
                        return False

        # If we successfully provide every customer, return True
        return True