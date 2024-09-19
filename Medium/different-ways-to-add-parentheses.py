# Author: Runar Fosse
# Time complexity: O(n2^n)
# Space complexity: O(n^22^n)

class Solution:
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y
    }
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Using dynamic programming

        # First split expression into numbers and operations
        self.expression, number = [], []
        for c in expression:
            if c in self.operations:
                self.expression.append("".join(number))
                self.expression.append(c)
                number = []
                continue
            number.append(c)
        self.expression.append("".join(number))

        # Then perform dynamic programming
        return self.opt(0, len(self.expression))
    
    @functools.cache
    def opt(self, s: int, e: int) -> List[int]:
        if s == e-1:
            return [int(self.expression[s])]
        
        # Iterate the current window of the expression
        results = []
        for i in range(s, e):
            if self.expression[i] not in self.operations:
                continue
            
            # Calculate all possible results from left and right side
            left_results = self.opt(s, i)
            right_results = self.opt(i+1, e)

            # And combine them in all possible ways using current operation
            operation = self.operations[self.expression[i]]
            for left in left_results:
                for right in right_results:
                    results.append(operation(left, right))
            
        # Finally return all possible current results
        return results


# opt(s, e) - Number of different results by computing the expression
#             expression[s:e] grouped in all possible ways.

# Base case:
# opt(i, i+1) = [expression[i]]

# Recurrency:
# opt(s, e) = [op(opt(s, i), opt(i+1, e)) for i in range(s, e)]
#             where op is the operation at expression[i]
#             for all i's where expression[i] is an operation

# N.o. states = 2^n
# Runtime per state = n
# Final time complexity -> O(n2^n)
# Space complexity is O(n^22^n) due to each state storing result of order n