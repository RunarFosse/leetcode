# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Using greedy

        # Sort by width in ascending, height by descending
        envelopes.sort(key=lambda env : (env[0], -env[1]))

        # Then we greedily find longest increasing subsequence of height
        # (Duplicate width values won't occur, due to sorting order)
        sequence = []
        for _, h in envelopes:
            # bisect_left binary searches index such that, if insertion of h
            # at index i, then sequence would maintain sorted order
            i = bisect_left(sequence, h)
            if i == len(sequence):
                sequence.append(h)
            else:
                sequence[i] = h

        return len(sequence)
    
