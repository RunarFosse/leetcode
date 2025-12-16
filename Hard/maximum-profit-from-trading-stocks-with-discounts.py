# Author: Runar Fosse
# Time complexity: O(nk^2)
# Space complexity: O(nk)

# where k is the budget

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # Using dynamic programming
        self.present, self.future, self.budget = present, future, budget
        
        # First, create the graph
        self.adjls = [[] for _ in range(n)]
        for u, v in hierarchy:
            self.adjls[u - 1].append(v - 1)
        
        # Then, iterate from the CEO
        profits = self.opt(0, False)
        return max(profits.values())
    
    @functools.cache
    def opt(self, i: int, discounted: bool) -> dict[int, int]:
        # Compute the profit of the current employee
        cost = (self.present[i] // 2) if discounted else self.present[i]
        profit = self.future[i] - cost

        # Create two dictionaries, one for buying (picking) current, other for skipping
        pick, skip = {cost: profit}, {0: 0}

        # Iterate every child
        for child in self.adjls[i]:
            # Compute buy all possibilities for the children
            child_discounted = self.opt(child, True)
            child_normal = self.opt(child, False)

            # Iterate given that current employee has bought
            new_pick = {}
            for cost, profit in pick.items():
                for child_cost, child_profit in child_discounted.items():
                    total_cost = cost + child_cost
                    if total_cost > self.budget:
                        continue
                    
                    total_profit = profit + child_profit
                    if total_cost not in new_pick or total_profit > new_pick[total_cost]:
                        new_pick[total_cost] = total_profit
            
            # Iterate given that current employee hasn't
            new_skip = {}
            for cost, profit in skip.items():
                for child_cost, child_profit in child_normal.items():
                    total_cost = cost + child_cost
                    if total_cost > self.budget:
                        continue
                    
                    total_profit = profit + child_profit
                    if total_cost not in new_skip or total_profit > new_skip[total_cost]:
                        new_skip[total_cost] = total_profit
            
            # And replace employee's dictionary
            pick, skip = new_pick, new_skip
        
        # Finally, merge dictionaries by picking costs with highest profits
        profits = {}
        for cost, profit in chain(pick.items(), skip.items()):
            if cost <= self.budget and (cost not in profits or profit > profits[cost]):
                profits[cost] = profit
        return profits
        
# opt(i, discounted) - Dictionary of costs with profits for employee i with/without 
#                      discounted price

# No. states = 2 * n
# Time complexity per state -> O(k^2)
# Space complexity per state -> O(k)

# Total time complexity => O(nk^2)
# Total space complexity => O(nk)
#           where k is the budget
