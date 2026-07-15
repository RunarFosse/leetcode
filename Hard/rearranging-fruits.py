# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # Using greedy

        # First, compute the frequency of each fruit in each basket
        frequencies, minimum = defaultdict(lambda: [0, 0]), inf
        for fruit1, fruit2 in zip(basket1, basket2):
            frequencies[fruit1][0] += 1
            frequencies[fruit2][1] += 1

            # Also store the minimum valued fruit
            minimum = min(fruit1, fruit2, minimum)
        
        # Then, extract the fruits to be transferred from each basket
        transfer1, transfer2 = [], []
        for fruit in frequencies.keys():
            # Otherwise, compute the difference
            difference = frequencies[fruit][0] - frequencies[fruit][1]

            # If the difference ever is odd, it is impossible to make baskets even
            if difference % 2 == 1:
                return -1

            # Move half the difference from either basket to the other
            fruits = [fruit] * abs(difference // 2)
            if difference > 0:
                transfer1.extend(fruits)
            elif difference < 0:
                transfer2.extend(fruits)
        
        # Sort the fruits to be transferred in ascending and descending order
        transfer1.sort()
        transfer2.sort(reverse=True)
        
        # And, greedily move the fruits to the other basket
        cost = 0
        for fruit1, fruit2 in zip(transfer1, transfer2):
            # By either moving them directly, or using a smaller value through 2 swaps
            cost += min(fruit1, fruit2, 2 * minimum)
        
        # Finally, return the minimum cost of making baskets equal
        return cost
