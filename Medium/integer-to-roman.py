# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        options = [(10, ("I", "V", "X")),
                   (100, ("X", "L", "C")),
                   (1000, ("C", "D", "M")),
                   (10000, ("M", None, None))]

        for (mod, (one, five, ten)) in options:
            rem = (num % mod - num % (mod // 10)) // (mod // 10)
            if rem <= 3:
                roman = one * rem + roman
            elif rem <= 8:
                roman = (one + five if rem == 4 else five + one * (rem % 5)) + roman
            else:
                roman = one + ten + roman

        return roman