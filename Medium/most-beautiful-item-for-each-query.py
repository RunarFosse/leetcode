# Author: Runar Fosse
# Time complexity: O((n + m)log n)
# Space complexity: O(n + m)

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # First sort items in ascending price, descending beauty
        items.sort(key=lambda e: (e[0], -e[1]))

        # Then iterate the items, keeping track of the most beauty per price
        best_items = [(0, 0)]
        for price, beauty in items:
            if price != best_items[-1][0]:
                best_items.append((price, max(beauty, best_items[-1][1])))  
        
        # Then at last, for each query
        answers = []
        for query in queries:
            # Binary search the most beautiful item
            index = bisect_right(best_items, query, key=lambda e: e[0])
            answers.append(best_items[index-1][1])

        return answers