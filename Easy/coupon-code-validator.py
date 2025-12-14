# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)

        # Declare a set of businesses which have valid coupons
        businesses = set(["electronics", "grocery", "pharmacy", "restaurant"])

        # Iterate the arrays
        valids = []
        for i in range(n):
            # Check if a given coupon is invalid, and remember it if so
            valid = code[i] and code[i].replace("_","a").isalnum()
            valid = valid and businessLine[i] in businesses and isActive[i]
            
            if valid:
                valids.append(i)
        
        # Finally, sort valid coupons, replace with their code and return
        valids.sort(key=lambda i: (businessLine[i], code[i]))
        return [code[i] for i in valids]
        