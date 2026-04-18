class Robot:

    def __init__(self, width: int, height: int):
        # Store the width and the height of the rectangle
        self.width, self.height = width - 1, height - 1

        # Store the position as a single number, denoting position along perimeter
        self.position = 0

        # Store if the robot has moved, because if not it should be position Eastwards
        self.moved = False

    def step(self, num: int) -> None:
        # Move the robot the given number of steps along the perimeter
        self.moved = True
        self.position += num
        self.position %= 2 * self.width + 2 * self.height

    def getPos(self) -> List[int]:
        # Transform position along perimeter to cartesian coordinates
        if self.position <= self.width:
            return [self.position, 0]
        if self.position <= self.width + self.height:
            return [self.width, self.position - self.width]
        if self.position <= 2 * self.width + self.height:
            return [2 * self.width - (self.position - self.height), self.height]
        return [0, 2 * self.height - (self.position - 2 * self.width)]
        
    def getDir(self) -> str:
        # The direction is fixed in regards to which edge the robot is walking along
        if self.position == 0:
            return "East" if not self.moved else "South"
        if self.position <= self.width:
            return "East"
        if self.position <= self.width + self.height:
            return "North"
        if self.position <= 2 * self.width + self.height:
            return "West"
        return "South"

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

# The given robot will always walk along the perimeter of the given rectangle.
# This makes the problem trivial.