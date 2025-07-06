class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        # Count frequency of each number in each array
        self.frequencies1, self.frequencies2 = defaultdict(int), defaultdict(int)
        for num in nums1:
            self.frequencies1[num] += 1
        for num in nums2:
            self.frequencies2[num] += 1

        # Also explicitly store nums2
        self.nums2 = nums2
        
    def add(self, index: int, val: int) -> None:
        # Update value in nums2 and decrement/increment frequencies
        self.frequencies2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.frequencies2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        # Iterate nums1
        pairs = 0
        for num, frequency in self.frequencies1.items():
            # Counting pairs equalling tot
            pairs += frequency * self.frequencies2[tot - num]
        return pairs

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)