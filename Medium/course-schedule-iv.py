# Author: Runar Fosse
# Time complexity: O(mnk)
# Space complexity: O(n^2)

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Using BFS

        # First create a graph
        self.adjls = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            self.adjls[a].append(b)
        
        # Then for each query
        answer = []
        for prerequisite, course in queries:
            # BFS and see if we can reach the course from the prerequisite
            answer.append(self.bfs(prerequisite, course))
    
        # Return all the answers
        return answer
    
    @functools.cache
    def bfs(self, prerequisite: int, course: int) -> bool:
        # If the courses are equal, they are reachable
        if prerequisite == course:
            return True
        
        # If the prerequisite has no neighbours, course is not reachable
        neighbours = self.adjls[prerequisite]
        if not neighbours:
            return False
        
        # Otherwise, check if course is reachable from neighbours
        return any(self.bfs(neighbour, course) for neighbour in neighbours)

        