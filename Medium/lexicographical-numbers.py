# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # Using trie
        numbers = []

        number = 1
        while len(numbers) < n:
            # Store current number
            numbers.append(number)

            # If we can traverse trie downwards, do so
            if number * 10 <= n:
                number *= 10
            
            # If we are at an end node, traverse back up
            elif number == n or number % 10 == 9:
                number //= 10
                while number % 10 == 9:
                    number //= 10
                number += 1
            
            # If neither, traverse rightwards
            else:
                number += 1
        
        # Finally, return all numbers in lexicographical order
        return numbers

# In this problem we are using a "implicitly defined" trie, where the tree
# and its traversal is represented in constant space, where the current node
# is represented by a number, and traversal of edges is represented
# by a function application on said number.

# These functions are:
# Adding another digit to lexicographic number -> Multiplying by 10
# Incrementing the current lexicographic number -> Adding 1
# Removing a digit and incrementing -> Integer division by 10 until unvisited
#                                      node and increment by 1