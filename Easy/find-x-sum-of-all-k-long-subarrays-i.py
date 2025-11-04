# Author: Runar Fosse
# Time complexity: O(nklog k)
# Space complexity: O(k)

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # Using sliding window
        n = len(nums)

        # Initially, count frequency of all (k-1)-first elements
        frequencies = defaultdict(int)
        for i in range(min(k, n)):
            frequencies[nums[i]] += 1
        
        # Slide a k-sized window over the array
        start, answer = 0, []
        for end in range(min(k, n), n + 1):
            # Compute X-sum of the current window
            frequents = sorted(frequencies.items(), key=lambda e: (e[1], e[0]))[-x:]
            answer.append(sum(num * frequency for (num, frequency) in frequents))

            # And move the window
            frequencies[nums[start]] -= 1
            start += 1
            if end < n:
                frequencies[nums[end]] += 1
        
        # Finally, return the answer array
        return answer
