# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Using counting
        n = len(sandwiches)

        # Count how many wants a square sandwich
        squares = sum(students)

        # Then iterate, "simulating" simulation of task
        i = 0
        for sandwich in sandwiches:
            # If front is a square sandwich
            if sandwich:
                # If squares == 0, no one can take front
                if not squares:
                    break

                # Remove 1 student from square sandwhich count
                squares -= 1
            
            # Else if front is a circle sandwich
            else:
                # If only squares left, no one can take front
                if squares == n - i:
                    break
                # If not, the front will be taken
            
            # Iterate front pointer if front was taken
            i += 1
            
        # Return the number of sandwiches taken
        return n - i
            
