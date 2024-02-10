# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def countSubstrings(self, s: str) -> int:
        # Using Manacher's Algorithm
        # https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
        
        # First add '|' between every char in s 
        string, m = "", 2*len(s) + 1
        for i in range(m):
            if i % 2:
                string += s[(i-1) // 2]
                continue
            string += '|'
        
        # Then we start the algorithm
        radii = [0] * m
        center, radius = 0, 0
        while center < len(string):
            
            # Find the current longest substring around center within the radius
            while center-(radius+1) >= 0 and center+(radius+1) < len(string) and string[center-(radius+1)] == string[center+(radius+1)]:
                radius += 1
            
            # Save the current radius within radius list
            radii[center] = radius

            # Increment center but store old values
            oldcenter, oldradius = center, radius
            center += 1
            radius = 0

            while center <= oldcenter + oldradius:
                # The current center lies within the palindrome defined by oldcenter
                # and oldradius, therefore we might reuse some of the precomputed info
                # avoiding redundant computations

                mirrorcenter = 2 * oldcenter - center
                mirrorradius = oldcenter + oldradius - center

                if radii[mirrorcenter] < mirrorradius:
                    radii[center] = radii[mirrorcenter]
                    center += 1
                elif radii[mirrorcenter] > mirrorradius:
                    radii[center] = mirrorradius
                    center += 1
                else:
                    radius = mirrorradius
                    break
        
        # For each radius stored in radii, 
        # calculate number of palindromes
        palindromes = 0
        for radius in radii:
            # If the current index is a palindrome,
            # use the radius size to calculate how many palindromes exist around
            if radius:
                palindromes += (radius - 1) // 2 + 1
    
        return palindromes

# This solution is heavily derived from the problem:
# "https://leetcode.com/problems/longest-palindromic-substring"
