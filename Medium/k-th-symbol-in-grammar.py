# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        
        if k > pow(2, n-2):
            k -= pow(2, n-2)
            return self.complement(self.kthGrammar(n-1, k))
        
        return self.kthGrammar(n-1, k)

    def complement(self, i: int):
        return 0 if i else 1
        
# 0
# 01
# 0110
# 01101001
# 0110100110010110
# 01101001100101101001011001101001
# 0110100110010110100101100110100110010110011010010110100110010110

# Emerging pattern, first half is always equal to last row
# second half is first half complemented

# Length of row n is equal to 2^n

# Given a k we find that given row m, row_m[k] == !row_m-1[k - 2^(m-1)]
# we also have that if k == 1, k is 0.