# Author: Runar Fosse
# Time complexity: O(2^n)
# Space complexity: O(n)

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # Using backtracking
        sequence = [0] * (2*n - 1)
        indices, seen = {}, [False] * (n + 1)
        self.backtrack(sequence, 0, n, indices, seen)
        return sequence
    
    def backtrack(self, sequence: List[int], i: int, n: int, indices: Dict[int, int], seen: List[bool]) -> bool:
        # If we have reached a valid end, return True
        if i == (2*n - 1):
            return True

        # If current index is already predetermined
        if i in indices:
            # Set it and continue
            sequence[i] = indices[i]
            return self.backtrack(sequence, i + 1, n, indices, seen)
        
        # Otherwise, loop every integer from largest to smallest
        for number in reversed(range(1, n + 1)):
            # If we've seen it before, or the next space is already occupied
            if seen[number] or (number > 1 and (i + number) in indices):
                # Skip
                continue

            # If not, try choosing the current number
            seen[number] = True
            sequence[i] = number

            # If it is bigger than 1, preset its other index
            if number > 1:
                indices[i + number] = number
            
            # And backtrack
            if self.backtrack(sequence, i + 1, n, indices, seen):
                return True
            
            # If this didn't give a valid sequence, remove and continue
            if number > 1:
                indices.pop(i + number)
            seen[number] = False

        # If we can't find a valid sequence, return False
        return False