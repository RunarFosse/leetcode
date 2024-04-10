# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Using greedy
        n = len(deck)

        # Sort the deck and turn into queue
        deck = deque(sorted(deck))

        # Simulate picking the indices from the deck, and build deck
        # to give output of drawing sorted in ascending order
        result = [0] * n
        indices = deque(range(n))
        while indices:
            result[indices.popleft()] = deck.popleft()
            if indices:
                indices.append(indices.popleft())
        
        # Return the resulting deck
        return result
