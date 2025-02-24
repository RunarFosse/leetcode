# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Using DFS

        # First create the graph
        self.adjls = defaultdict(list)
        for a, b in edges:
            self.adjls[a].append(b)
            self.adjls[b].append(a)
        
        # Then DFS Bob's path
        self.path = []
        self.bob(bob, set())
        print(self.path)
        
        # At last, DFS Alice's path while moving Bob
        self.amount = amount
        return self.alice(0, 0, set())
    
    def bob(self, bob: int, seen: Set[int]) -> bool:
        # Add current bob node to path
        self.path.append(bob)
        seen.add(bob)

        # If we've reached the end, return True
        if bob == 0:
            return True

        # DFS neighbours
        for neighbour in self.adjls[bob]:
            if neighbour not in seen:
                if self.bob(neighbour, seen):
                    return True
        
        # If we didn't reach the end, remove from path and return False
        self.path.pop()
        return False


    def alice(self, alice: int, step: int, seen: Set[int]) -> int:
        # Add current node to seen
        seen.add(alice)

        # Compute where Bob currently is
        bob = self.path[step] if step < len(self.path) else 0

        amount_alice = self.amount[alice]
        amount_bob = self.amount[bob]

        # Then compute current profit from step
        current = amount_alice
        if alice == bob:
            current /= 2

        # If we are at a leaf node, return
        if len(self.adjls[alice]) == 1 and self.adjls[alice][0] in seen:
            return current

        # Oherwise, set current amounts to 0
        self.amount[alice], self.amount[bob] = 0, 0

        # And continue DFS
        maximum = -1e12
        for neighbour in self.adjls[alice]:
            if neighbour not in seen:
                maximum = max(self.alice(neighbour, step + 1, seen), maximum)

        # Restore amount
        self.amount[alice], self.amount[bob] = amount_alice, amount_bob
        
        # Return maximum amount to be gained
        return int(current + maximum)
