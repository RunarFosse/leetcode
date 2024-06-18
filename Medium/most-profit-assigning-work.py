# Author: Runar Fosse
# Time complexity: O(mlog m + nlog n)
# Space complexity: O(m+n)

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Using greedy
        n = len(profit)

        # First sort workers in ascending level of skill
        worker.sort()

        # Then sort all jobs based on difficulty
        jobs = sorted(zip(difficulty, profit))

        # For each worker, greedily pick the most profitable 
        # job they can complete. (Storing most profitable for later workers)
        total_profit, best_job = 0, 0
        pointer = 0
        for skill in worker:
            while pointer < n and skill >= jobs[pointer][0]:
                best_job = max(jobs[pointer][1], best_job)
                pointer += 1
            
            # Add profit of most profitable completable job
            total_profit += best_job

        # Return total profit
        return total_profit