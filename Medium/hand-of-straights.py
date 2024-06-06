# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        
        # First check if hand is divisible by groupsize
        if n % groupSize:
            return False

        # Then, count frequency of each card
        frequencies = defaultdict(int)
        for card in hand:
            frequencies[card] += 1

        # At last, verify we can create groups of incremental value
        for card in hand:
            # If card is already used, skip
            if not frequencies[card]:
                continue

            # First, find the first card in this sequence
            start = card
            while frequencies[start-1]:
                start -= 1
            
            # Then verify group can be of created up until card
            while start <= card:
                while frequencies[start]:
                    # Verify group of groupSize can be created from start
                    for i in range(groupSize):
                        if not frequencies[start+i]:
                            return False
                        frequencies[start+i] -= 1
                start += 1

        # If we've used all cards, return True
        return True
