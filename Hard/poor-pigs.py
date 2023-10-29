# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # Solved analytically
        tests = minutesToTest // minutesToDie
        pigs = log(buckets, tests+1)

        # Python's log function sometimes suffer from floating point errors
        # Compensate for this here (removes float decimals behind 5th)
        pigs = trunc(pigs * 100000) / 100000

        return ceil(pigs)

# The number of different "tests" we have time to do is
# tests = minutesToTest / minutesToDie

# Given tests we know that the different possible ways to test on no. pigs, pigs
# is equal to combinations = (tests + 1) ^ pigs

# This is due to us allowing pigs not to get tested on in a given combinations
# (if not we would have "tests choose pigs" no. combinations instead)

# We know we have to test every bucket, i.e. combinations have to be greater than 
# or equal to the number of buckets. This could be rewritten to the number of buckets
# have to be less than or equal to the number of combinations, 
# i.e. a minimization problem! We want to minimize pigs subject to the equation
# buckets <= (tests + 1) ^ pigs

# Now, this is a problem which can easily be solved analytically, as
# log_(tests+1)(buckets) <= pigs. Voila, O(1) solution.