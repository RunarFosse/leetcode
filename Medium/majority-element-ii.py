class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1, c1 = None, 0
        n2, c2 = None, 0

        for n in nums:
            if (c1 == 0 or n1 == None) and n2 != n:
                n1 = n
            if (c2 == 0 or n2 == None) and n1 != n:
                n2 = n
            
            if n1 == n:
                c1 += 1
                continue
            if n2 == n:
                c2 += 1
                continue

            c1 -= 1
            c2 -= 1
        
        # Rerun to verify > floor(n / 3) occurences
        minc = floor(len(nums) / 3)
        c1, c2 = 0, 0
        for n in nums:
            if n1 == n:
                c1 += 1
            if n2 == n:
                c2 += 1

        if c1 > minc and c2 > minc:
            return [n1, n2]
        
        if c1 <= minc and c2 <= minc:
            return []
        
        return [n1] if c1 > minc else [n2]
        