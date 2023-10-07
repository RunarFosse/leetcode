# Author: Runar Fosse
# Time complexity: O(nm)
# Space complexity: O(m)

class Solution:
    map = { "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"] }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        combinations = [""]
        for digit in digits:
            combinations = [combination + c for c in self.map[digit] for combination in combinations]
        
        return combinations