# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        self.expression = expression
        return self.evaluate(0)[0]
    
    def evaluate(self, i: int) -> (bool, int):
        # Identify the current character
        char = self.expression[i]

        # If it is either True or False, return evaluation
        if char in ["t", "f"]:
            return (char == "t", i)
        
        # If the character is "!", return the logical NOT of the expression
        if char == "!":
            evaluation, index = self.evaluate(i + 2)
            return (not evaluation, index + 1)

        # If not, it is an operation with (possibly) several inner
        # expressions. First we evaluate these
        evaluations, pointer = [], i + 1
        while self.expression[pointer] != ")":
            # Evaluate the current expression
            evaluation, index = self.evaluate(pointer + 1)
            evaluations.append(evaluation)

            # Move pointer
            pointer = index + 1
        
        # Finally evaluate the whole current expression
        evaluation = all(evaluations) if char == "&" else any(evaluations)
        return (evaluation, pointer)