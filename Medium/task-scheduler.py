# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Using analytical solution

        # Find max_occurence, as well as how many have the same occurence
        max_occurences, tasks_of_max_occurences = 0, 0
        occurences = [0] * 26
        indexOf = lambda c : ord(c) - ord("A")
        for task in tasks:
            occurences[indexOf(task)] += 1
            if occurences[indexOf(task)] > max_occurences:
                max_occurences = occurences[indexOf(task)]
                tasks_of_max_occurences = 1
            elif occurences[indexOf(task)] == max_occurences:
                tasks_of_max_occurences += 1
        
        # Then compute intervals using formula and return
        intervals = (max_occurences - 1) * (n + 1) + tasks_of_max_occurences
        return max(intervals, len(tasks))

    
# We can solve this problem analytically.
# We know that a given task t1 has to have at least n tasks completed between
# each completion of itself. The total number of intervals to complete
# a single task t1 = (occurences_t1 - 1) * (n + 1)
# If we pick t1 as the maximum occuring one, we can fit all other between each
# completion of t1. If any other tasks occur as often as t1, we can complete
# them straight after t1, leading to a additional task completion at the end,
# or a simple addition to the formula.

# Therefore we have the resulting formula:
# intervals = (max_occurences - 1) * (n + 1) + tasks_of_max_occurences

# However, this formula might not hold if n < then the number of tasks
# between each completion of t1, therefore we return the max of this
# and the total number of tasks.