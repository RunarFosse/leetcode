# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Using greedy

        # Sort the tasks based on energy difference between minimum and actual
        tasks.sort(key=lambda task: task[1] - task[0])

        # Then, iterate the tasks
        initial = 0
        for actual, minimum in tasks:
            # Update the initial energy needed as either the minimum,
            # or a previous initial energy plus the actual used energy
            initial = max(initial + actual, minimum)
        
        # Finally, return this minimum initial energy to finish all tasks
        return initial
