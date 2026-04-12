# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minimumDistance(self, word: str) -> int:
        # Using dynamic programming
        self.n, self.word = len(word), word

        # Precompute the position of each of the characters
        self.character_positions = [(c % 6, c // 6) for c in range(26)]
        self.indexOf = lambda character: ord(character) - ord("A")

        # Then, return the minimum distance to type the word
        return self.opt(0, None, None)
    
    @functools.cache
    def opt(self, i: int, one: Optional[Tuple[int, int]], two: Optional[Tuple[int, int]]) -> int:
        # Base case
        if i == self.n:
            return 0
        
        # Get the target position of the current character
        target = self.character_positions[self.indexOf(self.word[i])]

        # Compute and return the minimum distance to type the rest of the word
        distance = min (
            self.opt(i + 1, target, two) + self.distance(one, target),
            self.opt(i + 1, one, target) + self.distance(two, target)
        )
        return distance

    
    def distance(self, position: Optional[Tuple[int, int]], target: Tuple[int, int]) -> int:
        # If position is None, we can pretend we always were at the target
        if position is None:
            return 0
        
        return abs(position[0] - target[0]) + abs(position[1] - target[1])


# opt(i, one, two) - Minimum distance to type word[i:] given 
#                    fingers one and two's positions.

# Base case:
# opt(n, _, _) = 0

# Recurrency:
# opt(i, one, two) = min(
#                opt(i + 1, char_pos[word[i]]], two) + distance(one, char_pos[word[i]]]),
#                opt(i + 1, one, char_pos[word[i]]]) + distance(two, char_pos[word[i]]]),
#                    )

# N.o. states = n * 26 * 26
# Time complexity per state -> O(1)
# Total time complexity => O(n)