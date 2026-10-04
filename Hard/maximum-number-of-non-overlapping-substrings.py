# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Using greedy
        n = len(s)

        # First, find the leftmost and rightmost occurence of each letter
        indexOf = lambda c: ord(c) - ord("a")
        leftmost, rightmost = [None] * 26, [0] * 26
        for i in range(n):
            index = indexOf(s[i])
            if leftmost[index] is None:
                leftmost[index] = i
            rightmost[index] = i
        
        # Then, iterate every character
        intervals = []
        for index in range(26):
            start = leftmost[index]
            if start is None:
                continue

            # Start at the leftmost position, moving temporarily towards its rightmost
            i, end, valid = start, rightmost[index], True
            while i <= end:
                # If we find a character with a leftmost occurence before our start
                c = s[i]
                if leftmost[indexOf(c)] < start:
                    # Then our current substring won't hold all occurences of every c
                    valid = False
                    break
                
                # Otherwise, possibly expand our search interval and continue iterating
                end = max(rightmost[indexOf(c)], end)
                i += 1
            
            # And store all such valid intervals
            if valid:
                intervals.append((start, end))
        
        # At last, sort all valid intervals in ascending order of end and start
        intervals.sort(key=lambda e: (e[1], e[0]))

        # And select the maximum number of non-overlapping intervals
        substrings, last = [], -1
        for left, right in intervals:
            # Turning each non-overlapping interval into their actual substring
            if left > last:
                substring = s[left:right + 1]
                substrings.append(substring)
                last = right
        
        # Finally, return this maximum number of non-overlapping substrings
        return substrings


# Time complexity is bounded by O(n) as the maximum number of intervals is 26.
# Sorting this is thus constant in time.
# Turning each interval into their non-overlapping substring is however linear
# in both time and space!