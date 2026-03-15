class Fancy:
    mod = int(1e9 + 7)
    def __init__(self):
        self.values = []
        self.multiplier = 1
        self.addend = 0

    def modMultInv(self, m: int) -> int:
        # Compute the modular multiplicative inverse
        return pow(m, self.mod - 2, mod=self.mod)

    def append(self, val: int) -> None:
        # Add the current number, taking into account current multiplier and addend
        value = ((val - self.addend) * self.modMultInv(self.multiplier)) % self.mod
        self.values.append(value)

    def addAll(self, inc: int) -> None:
        # Increment the current addend
        self.addend = (self.addend + inc) % self.mod

    def multAll(self, m: int) -> None:
        # Multiply both the multipler, and the addend
        self.multiplier = m * self.multiplier % self.mod
        self.addend = m * self.addend % self.mod

    def getIndex(self, idx: int) -> int:
        # Get the desired number, if within range
        if idx >= len(self.values):
            return -1
        return (self.multiplier * self.values[idx] + self.addend) % self.mod


# Fermat's Little Theorem gives us that, for a number x, if p is prime, then:
# x ^ (p - 1) = 1 (mod p)

# By this theorem, we also have that:
# x ^ (p - 2) = x^(-1) (mod p)

# Thus we can easily find the modular multiplicative inverse by exponentiating our
# number x by p - 2. Here, our modulus is a prime number, meaning this in our case holds.


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)