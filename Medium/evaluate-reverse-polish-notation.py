# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Using stack
        stack = []

        # Define the different operations' functionality
        operations = {
            "+" : lambda left, right: left + right,
            "-" : lambda left, right: left - right,
            "*" : lambda left, right: left * right,
            "/" : lambda left, right: int(left / right)
        }

        # Iterate the tokens
        for token in tokens:
            # If the token is an operation
            if token in ["+", "-", "*", "/"]:
                # Pop two last numbers and push result from operation application
                right, left = stack.pop(), stack.pop()
                stack.append(operations[token](left, right))
            # If the token is a number
            else:
                # Cast from string to int and push to stack
                stack.append(int(token))

        # Return the last remaining number
        return stack.pop()