# Author: Runar Fosse
# Time complexity: O(n^2log n)
# Space complexity: O(n)

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Using Divide and Conquer
        self.s, n = s, len(s)

        # First, compute the prefix sum of the string
        self.prefixes = [0]
        for c in s:
            prefix = self.prefixes[-1] + (1 if c == "1" else -1)
            self.prefixes.append(prefix)
        
        return self.orderSpecialString(0, n + 1)
        
    def orderSpecialString(self, start: int, end: int) -> str:
        # Iterate the substring, finding all troughs
        troughs = []
        for i in range(start + 1, end - 1):
            if self.prefixes[i - 1] > self.prefixes[i] < self.prefixes[i + 1]:
                troughs.append(i)

        # If there are no troughs, return the string
        if not troughs:
            return self.s[start:end]

        # Otherwise, iterate the troughs, splitting on the minimums
        minimum = min(self.prefixes[trough] for trough in troughs)
        troughs = deque(filter(lambda trough: self.prefixes[trough] == minimum, troughs))

        # Add start end to each of the split substrings
        s = next(i for i in range(start, end) if self.prefixes[i] == minimum)
        e = next(i for i in reversed(range(start, end)) if self.prefixes[i] == minimum)
        troughs.appendleft(s)
        troughs.append(e)

        # Extract each of the special substrings separated by troughs
        specials = [self.orderSpecialString(s, e) for s, e in pairwise(troughs)]

        # Order them in descending lexicographical order, and add to cover full substring
        specials = deque(sorted(specials, reverse=True))
        specials.appendleft(self.s[start:s])
        specials.append(self.s[e:end])

        # And return this special binary string
        return "".join(specials)
