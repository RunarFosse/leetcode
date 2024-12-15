# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Using greedy
        n = len(classes)

        # Iterate list of classes, computing how much we gain from adding
        # an extra passing student, and build a max-heap
        queue = []
        for i in range(n):
            passes, total = classes[i]
            gain = (passes + 1) / (total + 1) - passes / total
            heappush(queue, (-gain, passes, total))

        # Then greedily improve the classes with the highest gain
        for i in range(extraStudents):
            _, passes, total = heappop(queue)
            gain = (passes + 2) / (total + 2) - (passes + 1) / (total + 1)
            heappush(queue, (-gain, passes + 1, total + 1))
        
        # After adding extra students, return the average passing ratio
        return sum(map(lambda c: c[1] / c[2], queue)) / n