# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # Using Sorted Set
        n = len(nums)

        # Utilize a datastructure to efficiently handle sum of (k - 2) smallest elements
        minimums = KSmallestSum(k - 2)

        # Initialize the datastructure with the first (k - 2) elements
        for i in range(1, k - 1):
            minimums.add(nums[i])

        # Then slide a window over the array
        cost = minimums.sum + nums[k - 1]
        for i in range(k - 1, n - 1):
            # Shrink the window if spanning over the given distance
            if i - dist > 0:
                minimums.remove(nums[i - dist])
            
            # Expand the window to contain the current element
            minimums.add(nums[i])

            # And store the minimum possible cost
            cost = min(minimums.sum + nums[i + 1], cost)

        # Finally, return the total minimum cost
        return nums[0] + cost

class KSmallestSum():
    """ Efficient datastructure for finding sum of k smallest elements. """
    def __init__(self, k: int):
        self.k, self.sum = k, 0
        self.minimums = SortedList()
        self.others = SortedList()
    
    def balance(self):
        # While there are less than k minimum elements, add from others
        while len(self.minimums) < self.k and len(self.others) > 0:
            num = self.others.pop(0)
            self.minimums.add(num)
            self.sum += num
        
        # However if there are more, move the other way
        while len(self.minimums) > self.k:
            num = self.minimums.pop()
            self.others.add(num)
            self.sum -= num

    def add(self, num: int):
        if len(self.others) > 0 and num >= self.others[0]:
            self.others.add(num)
        else:
            self.minimums.add(num)
            self.sum += num
        self.balance()
    
    def remove(self, num: int):
        if num in self.minimums:
            self.minimums.remove(num)
            self.sum -= num
        else:
            self.others.remove(num)
        self.balance()
