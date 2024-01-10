# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # First we turn the tree into a adjacency list (undirected graph)
        adjls = defaultdict(list)
        queue = deque([root])
        while queue:
            node = queue.popleft()

            # Add left and right nodes if they exists
            # Also add edge back from them to node
            if node.left:
                queue.append(node.left)
                adjls[node.val].append(node.left.val)
                adjls[node.left.val].append(node.val)
            if node.right:
                queue.append(node.right)
                adjls[node.val].append(node.right.val)
                adjls[node.right.val].append(node.val)

        # Then perform BFS from the start node, returning the highest distance
        visited = set()
        queue.append((start, 0))
        while queue:
            # Check if next has already been visited, if so, drop it
            if queue[0][0] in visited:
                queue.popleft()
                continue
            node, distance = queue.popleft()
            visited.add(node)

            for neighbour in adjls[node]:
                queue.append((neighbour, distance+1))
        
        return distance

# This question asks us to find the maximum height of the tree, if
# the tree was rooted in the node "start".