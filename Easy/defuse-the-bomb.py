# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # Using prefix sum
        n = len(code)

        # If k is 0, return the zero array
        decrypted = [0] * n
        if not k:
            return decrypted
        
        # Start by computing sum of the last abs(k) numbers
        prefix = 0
        for i in range(n - abs(k), n):
            prefix += code[i]

        # For each entry in the code
        for i in range(n):
            # Replace with target sum
            if k < 0:
                decrypted[i] = prefix
            else:
                decrypted[i - k - 1] = prefix
            
            # And continue computing running prefix sum
            prefix -= code[i - abs(k)]
            prefix += code[i]

        # Finally return the decrypted code
        return decrypted