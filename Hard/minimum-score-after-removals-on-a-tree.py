# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # Using DFS
        n = len(nums)

        # First, create the graph
        self.adjls = defaultdict(list)
        for a, b in edges:
            self.adjls[a].append(b)
            self.adjls[b].append(a)
        
        # Initialize subtree XOR sums with current node value
        self.xors = nums

        # Also store entry and exit times for node inclusion check
        self.times = [None] * n

        # Then DFS from the root node
        self.dfs(0, 0, set())
        print(self.xors, self.times)

        # After removing two edges, we will have two new root nodes, iterate them
        score = 1e9
        for a in range(1, n):
            for b in range(a + 1, n):
                # If b is a subnode of a
                time_in, time_out = self.times[b]
                if time_in > self.times[a][0] and time_in < self.times[a][1]:
                    xor_1 = self.xors[0] ^ self.xors[a]
                    xor_2 = self.xors[a] ^ self.xors[b]
                    xor_3 = self.xors[b]
                
                # Else if a is a subnode of b
                elif time_in < self.times[a][0] and time_out > self.times[a][0]:
                    xor_1 = self.xors[0] ^ self.xors[b]
                    xor_2 = self.xors[b] ^ self.xors[a]
                    xor_3 = self.xors[a]
                
                # Otherwise they are in disjoint trees
                else:
                    xor_1 = self.xors[0] ^ self.xors[a] ^ self.xors[b]
                    xor_2 = self.xors[a]
                    xor_3 = self.xors[b]
                
                # Compute the difference and store the minimum score
                difference = max(xor_1, xor_2, xor_3) - min(xor_1, xor_2, xor_3)
                score = min(difference, score)
        
        # Finally, return the minimum score when removing two edges
        return score

    def dfs(self, node: int, entry: int, seen: Set[int]) -> int:
        # Mark the current node as seen
        seen.add(node)

        # Iterate each of the child nodes
        time = entry
        for child in self.adjls[node]:
            if child in seen:
                continue
            time = self.dfs(child, time + 1, seen)
            
            # Store to subtree XOR
            self.xors[node] ^= self.xors[child]
        
        # Store entry and exit times and return
        self.times[node] = (entry, time)
        return time + 1
        