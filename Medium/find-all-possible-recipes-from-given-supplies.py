# Author: Runar Fosse
# Time complexity: O(n + m + k)
# Space complexity: O(n + m + k)

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Using Topological Sorting
        n = len(recipes)

        # First create the graph
        adjls, indegrees = defaultdict(list), defaultdict(int)
        for i in range(n):
            recipe = recipes[i]
            for ingredient in ingredients[i]:
                adjls[ingredient].append(recipe)
                indegrees[recipe] += 1

        # Then, continue removing recipes until termination
        dishes, queue = [], deque(supplies)
        while queue:
            dish = queue.popleft()
            for recipe in adjls[dish]:
                indegrees[recipe] -= 1
                if indegrees[recipe] == 0:
                    dishes.append(recipe)
                    queue.append(recipe)

        # Finally, return all finished dishes
        return dishes
        