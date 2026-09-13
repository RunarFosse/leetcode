# Author: Runar Fosse
# Time complexity: O(n^4)
# Space complexity: O(n^2)

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        # First, iterate each cell in each image
        ones1, ones2 = [], []
        for i in range(n):
            for j in range(n):
                # Collecting cells with a 1 bit
                if img1[i][j]:
                    ones1.append((i, j))
                if img2[i][j]:
                    ones2.append((i, j))
        
        # Then, iterate each pair of 1 bit cells
        translations = defaultdict(int)
        for i1, j1 in ones1:
            for i2, j2 in ones2:
                # Counting the overlap per translation
                translations[(i1 - i2, j1 - j2)] += 1
        
        # Finally, return the maximum overlap of all translations
        return max(translations.values(), default=0)
