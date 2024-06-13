# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def compress(self, chars: List[str]) -> int:
        # Using greedy
        n = len(chars)
        
        # Iterate each letter in chars
        pointer, current_length = 0, 1
        for i in range(n):
            # If we are at the end, or the next char is different to current
            if i == n-1 or chars[i] != chars[i+1]:
                # Compress by first denoting character
                chars[pointer] = chars[i]
                pointer += 1

                # Then length, if and only if length is bigger than 1
                if current_length > 1:
                    for c in str(current_length):
                        chars[pointer] = c
                        pointer += 1
                
                # Reinitialize new sequence length to 1
                current_length = 1

            # If not, increment size of current homogeneous sequence
            else:
                current_length += 1
        
        # Pointer size denotes size of new array
        return pointer