from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Initialize a sorted set per cuisine
        self.foodratings = defaultdict(SortedSet)
        # Store the cuisine and rating given a food, + add them to cuisines sets
        # (Storing negative rating allow for sorted in "descending" order)
        self.ratings = {}
        self.cuisines = {}
        for i in range(len(foods)):
            food, rating, cuisine = foods[i], ratings[i], cuisines[i]
            self.ratings[food] = rating
            self.cuisines[food] = cuisine
            self.foodratings[cuisine].add((-rating, food))


    def changeRating(self, food: str, newRating: int) -> None:
        # First remove old element from foodratings set
        cuisine = self.cuisines[food]
        self.foodratings[cuisine].remove((-self.ratings[food], food))

        # Then add new element
        self.foodratings[cuisine].add((-newRating, food))

        # And update ratings dictionary
        self.ratings[food] = newRating
        

    def highestRated(self, cuisine: str) -> str:
        # Return name of food in the front of cuisines sorted set
        return self.foodratings[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)