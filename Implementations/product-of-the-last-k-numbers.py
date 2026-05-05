class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]
        self.size = 0

    def add(self, num: int) -> None:
        # If added number is zero, reset products
        if num == 0:
            self.prefix = [1]
            self.size = 0
        else:
            # If not, add it as normal
            self.prefix.append(self.prefix[-1] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            # If k runs over a 0, product is 0
            return 0
        
        # If not, return the product of the k last numbers
        return self.prefix[-1] // self.prefix[-k-1] 


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)