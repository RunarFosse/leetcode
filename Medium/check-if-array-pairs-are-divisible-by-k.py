# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(k)

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)

        # First, replace every number with its modulo k
        for i in range(n):
            arr[i] %= k
        
        # Then iterate the array
        modulos = [0] * k
        for i in range(n):
            modulo = arr[i]

            # In case the modulo is 0, pair up with already existing 0
            if modulo == 0:
                modulos[modulo] += -1 if modulos[modulo] else 1
                continue

            # If not, but current modulo has reverse seen, pair together
            if modulos[k - modulo]:
                modulos[k - modulo] -= 1

            # If not, remember current modulo
            else:
                modulos[modulo] += 1

        # If every modulo has been paired, return true
        return not any(modulos)