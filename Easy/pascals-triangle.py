class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        # Generate whole triangle
        for i in range(1,numRows):
            triangle.append([])
            # Generate (first half) row
            for j in range(floor(i/2)+1):
                triangle[i].append(triangle[i-1][j])
                if j > 0:
                    triangle[i][j] += triangle[i-1][j-1]
            # Generate rest
            for j in range(floor(i/2)+1, i+1):
                triangle[i].append(triangle[i][i-j])
        
        return triangle


# Pascal's triangle rows are symmetrical, meaning we only
# need to calculate the first half of the row.