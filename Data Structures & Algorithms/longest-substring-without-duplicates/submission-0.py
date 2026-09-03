class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        longest = 0
        left = 0
        right = 0
        
        while right < n:
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
                longest = max(longest, right - left + 1)
                right += 1
        return longest


        