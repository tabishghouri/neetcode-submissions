class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            # get the count of each char
            seen[s[right]] = seen.get(s[right], 0) + 1

            # find the most common char in seen
            most_common = max(seen.values())

            # while window size - most_common = replacements needed > k:
            # we shrink the left side of window
            while (right - left + 1) - most_common > k:
                seen[s[left]] -= 1
                left +=1
            longest = max(longest, right - left + 1)

        return longest


        