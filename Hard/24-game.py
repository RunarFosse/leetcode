# Author: Runar Fosse
# Time complexity: O(3^n * (n!)^2)
# Space complexity: O(n)

from fractions import Fraction

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # Using backtracking

        # To prevent floating-point imprecision, use fractions
        self.cards = [Fraction(card) for card in cards]
        return self.backtrack()

    def backtrack(self) -> bool:
        # If there is only one card left
        n = len(self.cards)
        if n == 1:
            # Verify it is 24
            return self.cards[0] == 24

        # Iterate every pair of available cards
        for i in range(n):
            for j in range(i + 1, n):
                # Combine two and two cards together
                a, b = self.cards[i], self.cards[j]
                combinations = {a + b, a - b, b - a, a * b}

                # Ensure we don't divide by zero
                if a != 0:
                    combinations.add(b / a)
                if b != 0:
                    combinations.add(a / b)
                
                # Temporarily remove the second selected card
                self.cards.pop(j)

                # And check if either combination results in 24
                for combined in combinations:
                    # By replacing the first current card with combination
                    self.cards[i] = combined

                    # And verifying
                    if self.backtrack():
                        return True
                
                # If no valid combination is found, restore the selected cards
                self.cards[i] = a
                self.cards.insert(j, b)
        
        # If no combination results in 24, return False
        return False
