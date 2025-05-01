# Author: Runar Fosse
# Time complexity: O((m + n)^2log(m + n))
# Space complexity: O(m + n)

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # Using binary search
        m, n = len(tasks), len(workers)

        # First, sort tasks and workers in ascending order
        self.tasks = sorted(tasks)
        self.workers = sorted(workers)

        # Then, binary search the answer
        answer, left, right = 0, 1, min(m, n)
        while left <= right:
            pivot = (left + right) // 2
            if self.canAssign(pivot, pills, strength):
                answer = pivot
                left = pivot + 1
            else:
                right = pivot - 1

        # Finally, return the number of tasks we can assign
        return answer
    
    def canAssign(self, k: int, pills: int, strength: int) -> bool:
        # Select the k strongest workers
        workers = deque(self.workers[-k:])
        
        # And iterate the k easiest tasks
        for i in range(k):
            task = self.tasks[k - i - 1]

            # If we can, select the strongest worker
            if workers[-1] >= task:
                workers.pop()
                continue

            # If not, find the strongest worker with a pill
            index = bisect_left(workers, task - strength)
        
            # If we are out of pills, or have no worker to do the job, return
            if not pills or index == len(workers):
                return False

            # And remove the pilled worker
            workers.remove(workers[index])
            pills -= 1

        return True