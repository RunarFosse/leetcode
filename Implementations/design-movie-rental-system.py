class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        # Store the price of each movie, per shop
        self.prices = {}

        # Store price and shop for each unrented movie in a sorted set
        self.unrented = defaultdict(SortedSet)

        # Store all rented movies globally in a sorted set
        self.rented = SortedSet()

        # And add all movies
        for shop, movie, price in entries:
            self.prices[(shop, movie)] = price
            self.unrented[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        # Given the movie, extract the 5 cheapest shops
        shops = []
        for _, shop in self.unrented[movie][:5]:
            shops.append(shop)
        return shops

    def rent(self, shop: int, movie: int) -> None:
        # Rent an unrented copy of the movie, from the shop
        price = self.prices[(shop, movie)]
        self.unrented[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        # Return a rented copy of the movie, to the shop
        price = self.prices[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.unrented[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        # Find the 5 cheapest rented movies
        rented = []
        for _, shop, movie in self.rented[:5]:
            rented.append((shop, movie))
        return rented


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()