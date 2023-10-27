# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def longestPalindrome(self, s: str) -> str:
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
            
        # Find longest substring, as we are currently only storing radius
        lps = ""
        for center, radius in enumerate(radii):
            if radius > len(lps):
                # Go from string to s
                c = center // 2
                r = radius // 2
                lps = s[c-r:c+r+1] if center % 2 else s[c-r:c+r]

        return lps


        