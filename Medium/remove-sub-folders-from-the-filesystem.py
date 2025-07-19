# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Using greedy
        n = len(folder)

        # First, sort the folders in lexicographically ascending order
        folder.sort()
        
        # The first folder is guaranteed to not be a sub-folder
        folders = [folder[0]]
        
        # Iterate the rest of the folders
        for i in range(1, n):
            # Take the last folder and append a forward-slash
            current, last = folder[i], folders[-1] + "/"

            # If the current folder doesn't start with said last folder
            if not current.startswith(last):
                # Then current is not a sub-folder and we can add it
                folders.append(current)
        
        # Finally, return all non sub-folders
        return folders