class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                current = num
                streak = 1
                while current + 1 in numSet:
                    current += 1
                    streak += 1

                longest = max(longest, streak)
        
        return longest
