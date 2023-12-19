# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # Using convolutions
        m, n = len(img), len(img[0])

        # For each cell as the convolution center
        # we perform the convolution and store the result
        for i in range(m):
            for j in range(n):
                # Find the average of the ("up-to") 3x3 matrix around the cell
                y_kernel = range(max(0,i-1), min(m,i+2))
                x_kernel = range(max(0,j-1), min(n,j+2))
                kernel_sum = sum(img[y][x] & 255 for x in x_kernel for y in y_kernel)
                kernel_size = len(y_kernel) * len(x_kernel)

                # Encode colvolved value into image color
                img[i][j] += (kernel_sum // kernel_size) << 8
        
        # Retrieve the encoded new convolved values from the image
        for i in range(m):
            for j in range(n):
                img[i][j] >>= 8

        return img

# Time complexity is O(mn) as we at max do 3x3 operations for every cell.
# This means that it is O(9mn) => O(mn).

# Space complexity is O(1) as we store each convolved value "encoded" into the already
# stored color value, meaning no extra used space!
# This is possible as each color stored in img is between 0 and 255. I.e. the first 8 bits.
# Therefore, we can store the convolved value in the 9-16 bits!
# We only need to remember to retrieve them back before returning, and keep them out
# of any of the other following convolution calculations.