# Author: Runar Fosse
# Time complexity: O(sqrt(n))
# Space complexity: O(1)

class Solution:
    def numSquares(self, n: int) -> int:
        # Analytical solution

        # If n is a perfect square, solution is trivial
        if self.isPerfect(n):
            return 1

        # First get rid of any multiples of 4 from n
        while not n % 4:
            n /= 4
        
        # Then we can check if the number was on the form 4^a(8b + 7)
        if n % 8 == 7:
            # If so, using Lagrange's four-square theorem we have that
            return 4
        
        # If not, we have check if n can be created using two perfect squares
        for square in map(lambda i: i*i, range(1, 101)):
            if square > n:
                break
            if self.isPerfect(n - square):
                return 2

        # If not, using Legendre's three-square theorem we have that
        return 3
    
    def isPerfect(self, n: int) -> bool:
        # n is perfect if the square root is an integer
        root = sqrt(n)
        return int(root) == root
        
# If we use Legendre's three-square theorem 
# ("https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem") 
# together with Lagrange's four-square theorem
# ("https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem")
# we can solve this problem optimally.