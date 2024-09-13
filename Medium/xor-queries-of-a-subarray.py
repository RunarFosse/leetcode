# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m + n)

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Using prefix XOR sum

        # First calculate the prefix XOR sums
        prefixes = [0]
        for num in arr:
            prefixes.append(prefixes[-1] ^ num)
        
        # Then compute every query answer
        answer = []
        for left, right in queries:
            answer.append(prefixes[right+1] ^ prefixes[left])
        
        # Finally return the answers
        return answer
        
# We have that for every number x, x ^ x = 0. Therefore we can calculate an
# XOR prefix sum array, making it such that for a query = [left, right],
# the answer arr[left] ^ arr[left+1] ^ ... ^ arr[right] is equal to
# prefix[right] ^ prefix[left] (as every number XOR summed into prefix[left]
# will be cancelled out and removed from prefix[right])!