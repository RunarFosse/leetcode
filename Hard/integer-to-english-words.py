# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(log n)

class Solution:
    # Store string representation of numbers and separators
    ones = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    separators = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int, iteration: int = 0) -> str:
        if not num:
            return "" if iteration else "Zero"

        # Turn the last 3 digits into words
        suffix = self.wordify(num % 1000)
       
        # Turn the other digits into words
        prefix = self.numberToWords(num // 1000, iteration + 1)

        # Get the current separator
        separator = self.separators[iteration]

        # Construct and return the full word
        words = []
        if prefix:
            words.append(prefix)
        if suffix:
            words.append(suffix)
            if separator:
                words.append(separator)

        return " ".join(words)

    def wordify(self, num: int) -> str:
        hundreds, tens, ones = num//100, (num%100)//10, num%10
        string = []

        # Stringyfy number iteratively
        if hundreds:
            string.append(self.ones[hundreds-1])
            string.append("Hundred")

        if tens == 1 and ones:
            string.append(self.teens[ones-1])
        else:
            if tens:
                string.append(self.tens[tens-1])
            if ones:
                string.append(self.ones[ones-1])
        
        return " ".join(string)

# From the example we can easily see that we have several equivalent
# parts, namely X Hundred Y Z, separated by Million, Thousand, etc.
# As num is bounded by integer precision, we only need to support
# separators up to a Billion (as 2^31 ≈ 2 billion).