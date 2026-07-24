# Author: Runar Fosse
# Time complexity: O(mlog m + n)
# Space complexity: O(m)

# where m is the maximum value in the array

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # Using Fast Walsh-Hadamard transform

        # First, the transform size is the maximum power of two bigger every value in nums
        size = 1 << max(nums).bit_length()

        # Then, count the frequency of all elements in nums
        frequencies = [0] * size
        for num in nums:
            frequencies[num] += 1
        
        # Apply the Fast Walsh-Hadamard transform, moving us into bit-parity space
        self.fwht(frequencies)

        # Apply two XOR convolutions through cubing each frequency value
        for value in range(size):
            frequencies[value] = pow(frequencies[value], 3)
        
        # Apply the inverse transform, moving us back into actual value space
        self.fwht(frequencies, inverse=True)

        # And count the number of unique values!
        return sum(1 for value in range(size) if frequencies[value] > 0)

    def fwht(self, values: List[int], inverse: bool = False) -> None:
        # Compute the Fast Walsh-Hadamard transform
        size = len(values)

        # At each stage of the transformation, iterate each bit
        bits = 0
        while bits < size.bit_length() - 1:
            length = 1 << bits
            for i in range(0, size, 2 * length):
                for j in range(i, i + length):
                    # Get two values with have different parity of the current bit
                    a, b = values[j], values[j + length]

                    # And apply the Hadamard butterfly to them
                    values[j] = a + b
                    values[j + length] = a - b
            
            # Then continue with the next bit
            bits += 1

        # If not applying the inverse transform, we are finished
        if not inverse:
            return
        
        # Applying the transform twice multiplies each element by the number of values
        # Thus to apply the inverse we only need to normalize after second application
        for value in range(size):
            values[value] //= size


# We want to find the unique results of XOR triplets.

# Finding all unique XOR pairs requires us to XOR every value over every other value,
# and storing the unique results.
# This can be thought of as a XOR convolution!

# By finding the unique results to every XOR triplet we would have to XOR every value
# over every unique result from that previous convolution – also a convolution!

# In short, finding every distinct XOR triplet result is equal to finding all
# unique results from two XOR convolutions over all the values!
# values *(xor) values *(xor) values

# Similar to how the Fast Fourier transform makes us able to perform convolutions
# through multiplications
# (i.e. two convolutions over f would just be F^3 in frequency space),
# there exists a Walsh-Hadamard transform making us able to perform
# XOR convolutions through multiplications!

# This would make us compute values *(xor) values *(xor) values as V^3!