# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # First count occurence of each element in the formula
        self.n = len(formula)
        elements, _ = self.countElements(0, formula)

        # And return them, sorted in the keys' lexicographical order
        items = sorted(elements.items())
        toString = lambda e, count : e + (str(count) if count > 1 else "")
        return "".join(toString(element, count) for element, count in items)
    
    def countElements(self, i: int, formula: str) -> (Dict[str, int], int):
        elements = defaultdict(int)

        # Iterate the formula
        while i < self.n:
            # If we reach a starting paranthesis, recurse
            if formula[i] == "(":
                sub_elements, sub_i = self.countElements(i+1, formula)
                i = sub_i + 1

                # If the next character is a number, multiply counts
                multiplier = 0
                if not (i < self.n and formula[i].isnumeric()):
                    multiplier = 1
                else:
                    while i < self.n and formula[i].isnumeric():
                        multiplier = multiplier * 10 + int(formula[i])
                        i += 1
                
                # Then add sub_element counts to current
                for key, val in sub_elements.items():
                    elements[key] += val * multiplier

                # And continue iterating
                continue
            
            # However if we reach an ending, return from current call
            if formula[i] == ")":
                return elements, i
            
            # If neither are true, add current element to count
            element = [formula[i]]
            i += 1
            while i < self.n and formula[i].islower():
                element.append(formula[i])
                i += 1
            element = "".join(element)
            
            # If a number comes after, multiply current element addition
            multiplier = 0
            if not (i < self.n and formula[i].isnumeric()):
                multiplier = 1
            else:
                while i < self.n and formula[i].isnumeric():
                    multiplier = multiplier * 10 + int(formula[i])
                    i += 1
            
            # Add count and continue iteration
            elements[element] += multiplier
        
        # On termination, return total element count
        return elements, i