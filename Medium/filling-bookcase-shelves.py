# Author: Runar Fosse
# Time complexity: O(nk)
# Space complexity: O(n)

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # Using dynamic programming
        n = len(books)
        opt = [0] * (n+1)

        for i in reversed(range(n)):
            width, height = books[i]

            # By default, build a new shelf to hold the book
            opt[i] = height + opt[i+1]
            current_height = height
            current_width = shelfWidth - width

            # Fill shelf with other books (until it can't hold anymore)
            for j in range(i+1, n):
                new_width, new_height = books[j]
                if current_width < new_width:
                    break

                current_height = max(new_height, current_height)
                current_width -= new_width

                opt[i] = min(opt[i], current_height + opt[j+1])
        
        # Return the minimum height of all shelves holding all books
        return opt[0]


# opt(i) - Minimum height of all shelves storing books books[i:]

# Base case:
# opt(n) = 0

# Recurrency:
# opt(i) = min(opt(j) + current_height for j in range(i+1, n)
#              if current_width > 0)
#              where current_height is the maximum height of all
#                    books in the interval books[i:j+1]
#                and current_width the cumulative width of all
#                    books on the same interval

# N.o. states = n
# Runtime per state is O(k) (where k is shelfWidth)
# -> Total time complexity of O(nk)