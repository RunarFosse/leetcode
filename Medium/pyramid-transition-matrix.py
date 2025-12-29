# Author: Runar Fosse
# Time complexity: O(n6^n)
# Space complexity: O(n^2)

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Using backtracking

        # First, create a mapping from the two base blocks to every allowed top block
        self.mapping = defaultdict(list)
        for c1, c2, c3 in allowed:
            self.mapping[c1 + c2].append(c3)
        
        # Then build the pyramid
        return self.build(bottom)
    
    @functools.cache
    def build(self, string: str) -> bool:
        # If the given string has a length of 1, then the pyramid is finished
        if len(string) == 1:
            return True
        
        # Otherwise, check if any possible new row finishes the pyramid
        return any(self.build(row) for row in self.backtrack(string, [], 0))
                
    def backtrack(self, string: str, current: List[str], i: int) -> Iterable[str]:
        # If we are at the end index, finish this row
        if i >= len(string) - 1:
            yield "".join(current)
            return

        # Otherwise, build every possible next string
        bottom = string[i:i + 2]
        for top in self.mapping[bottom]:
            current.append(top)
            # And yield every possible allowed row
            yield from self.backtrack(string, current, i + 1)
            current.pop()
            