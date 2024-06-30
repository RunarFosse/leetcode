# Author: Runar Fosse
# Time complexity: O(n+m)
# Space complexity: O(n+m)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Using topological sorting

        # First construct a directed graph, where each edge (a, b) means that
        # node a is a prerequisite to node b. Also count indegree of each node.
        indegrees = [0] * numCourses
        adjls = [[] for _ in range(numCourses)]
        for c1, c2 in prerequisites:
            indegrees[c1] += 1
            adjls[c2].append(c1)
        
        # Traverse graph using topological sorting, counting courses
        # you possibly can take
        courses_taken = 0
        queue = deque([i for i in range(numCourses) if not indegrees[i]])
        while queue:
            course = queue.popleft()
            courses_taken += 1
            
            # Taking the current course means one less prerequisite
            # to take for the courses connected to this one
            for neighbour in adjls[course]:
                indegrees[neighbour] -= 1
                if not indegrees[neighbour]:
                    queue.append(neighbour)
            
        # Return if all courses can be taken or not
        return courses_taken == numCourses