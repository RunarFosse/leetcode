# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Using segment tree

        # First, iterate all the squares and gather all horizontal edges
        xs, horizontals = set(), []
        for x, y, length in squares:
            horizontals.append((y, x, x + length, True))
            horizontals.append((y + length, x, x + length, False))

            # Also store x-coordinate corners in a set
            xs.update([x, x + length])
        
        # Then, sort x-coordinates and horizontal's y-coordinate in ascending order
        horizontals.sort()
        xs = sorted(xs)

        # Use a segment tree to count total non-overlapping width of squares under line
        width = SegmentTree(xs) 

        # Then, scan a horizontal line over all the squares, keeping track of area under
        area, y_last = 0, 0
        areas, widths = [], []
        for y, x_left, x_right, starts in horizontals:
            # Get the last height difference
            difference = y - y_last

            # Get the current width of squares under the scanline and expand area
            current_width = width.query()
            area += difference * current_width

            # Add or remove new square from segment tree
            width.update(1, 0, width.length - 1, x_left, x_right, starts)

            # Store current width and total area in array
            areas.append(area)
            widths.append(current_width)

            # And update this as the last seen y-coordinate
            y_last = y
        
        # Finally, compute half the area, rounded up
        split = (area + 1) // 2

        # Binary search it's occurence in the area array
        index = bisect_left(areas, split)

        # Extract the square width at that index, as well as y-coordinate
        current_area = areas[index]
        current_width = widths[index]
        y = horizontals[index][0]

        # Compute the excess, and how much we must reduce the height by
        excess = 2 * current_area - area
        reduction = excess / (current_width * 2)

        # And use this reduction to return the minimum splitting y-coordinate
        return y - reduction

class SegmentTree():
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.length = len(xs) - 1
        self.edges = [0] * (4 * self.length)
        self.widths = [0] * (4 * self.length)
    
    def update(self, node: int, left: int, right: int, query_left: int, query_right: int, starts: bool) -> None:
        # If interval is outside query interval, return early
        if self.xs[right + 1] <= query_left or self.xs[left] >= query_right:
            return
        
        # If we are fully inside the query interval, we have the full information
        if self.xs[left] >= query_left and self.xs[right + 1] <= query_right:
            self.edges[node] += 1 if starts else -1
        else:
            # Otherwise, split and recurse
            pivot = (left + right) // 2
            self.update(node << 1, left, pivot, query_left, query_right, starts)
            self.update((node << 1) + 1, pivot + 1, right, query_left, query_right, starts)

        # Then, if this node has any edges fully covering it
        if self.edges[node] > 0:
            # Compute the actual non-overlapping width these edges are covering
            self.widths[node] = self.xs[right + 1] - self.xs[left]
            return
        
        # If not, and interval is a singleton
        if left == right:
            # It does not cover any width
            self.widths[node] = 0
            return
        
        # Finally if not, use children's information to compute current coverage
        self.widths[node] = self.widths[node << 1] + self.widths[(node << 1) + 1]

    def query(self):
        # Return the total non-overlapping width covered by squares
        return self.widths[1]
