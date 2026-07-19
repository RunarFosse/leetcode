# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # Using Merkle trie

        # First, construct the trie from the given paths
        trie = Node()
        for path in paths:
            current = trie
            for folder in path:
                if folder not in current.children:
                    current.children[folder] = Node()
                current = current.children[folder]
        
        # Then, traverse the trie and compute Merkle hashes
        self.seen = defaultdict(int)
        self.dfs(trie, is_root=True)

        # Finally, traverse the trie again, removing nodes with identical Merkle hashes
        queue, remaining = deque([([], trie)]), []
        while queue:
            path, node = queue.popleft()
            if self.seen[node.hash] > 1:
                continue
            
            # If the folder remains and it is not the root
            if path:
                # Add path to remaining folders
                remaining.append(path)

            # And continue traversing down to children
            for folder, child in node.children.items():
                queue.append((path + [folder], child))

        # Returning the remaining folders after deletion
        return remaining
    
    def dfs(self, node: Node, is_root: bool = False) -> None:
        # Concatenate all child names and hashes in lexicographic order
        hashes = []
        for name, child in sorted(node.children.items()):
            self.dfs(child)
            hashes.append((name, str(child.hash)))
        
        # For every non-root, non-leaf node, mark the hash and increment seen count
        if not is_root and hashes:
            node.hash = hash(tuple(hashes))
            self.seen[node.hash] += 1

# A Merkle trie node, containing
# children as well as their hash
class Node():
    def __init__(self):
        self.children = {}
        self.hash = 0
