# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Using two pointer
        s_new = []

        # Count frequency of each character
        frequencies = [0] * 26
        for c in s:
            frequencies[ord(c) - ord("a")] += 1
    
        # Then iterate frequencies from behind
        left, right = 24, 25
        while right >= 0:
            # Move pointers if needed
            if not frequencies[right]:
                while left >= 0 and not frequencies[left]:
                    left -= 1
                right = left
                left -= 1
            
            # Add as many as we can from right pointer to string
            additions = min(frequencies[right], repeatLimit)
            frequencies[right] -= additions
            s_new.append(chr(right + ord("a")) * additions)

            # If there are any remaining, add a separator from left pointer
            if frequencies[right]:
                while left >= 0 and not frequencies[left]:
                    left -= 1
                
                # If we cannot add more separators, break
                if left < 0:
                    break

                frequencies[left] -= 1
                s_new.append(chr(left + ord("a")))

        # Return the new string
        return "".join(s_new)