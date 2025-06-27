# Author: Runar Fosse
# Time complexity: O(n(n/k)!)
# Space complexity: O((n/k)!)

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # First, count the frequency of each character
        indexOf = lambda c: ord(c) - ord("a")
        frequencies = [0] * 26
        for c in s:
            frequencies[indexOf(c)] += 1

        # Filter the characters with a frequency of at least k
        repeated = [chr(i + ord("a")) for i in range(26) if frequencies[i] >= k]
        
        # Then, add each character with a frequency of k to a queue
        substring = ""
        queue = deque(repeated)
        while queue:
            # Get the first candidate subsequence
            current = queue.popleft()

            # Store the largest valid substring
            if len(current) >= len(substring):
                substring = current

            # For each other k-repeated characters
            for c in repeated:
                # Check if the composite substring is repeated k times
                composite = current + c
                string = iter(s)
                if all(char in string for char in composite * k):
                    # If so, add it as a new candidate
                    queue.append(composite)
        
        # Finally, return the longest k-repeated substring
        return substring