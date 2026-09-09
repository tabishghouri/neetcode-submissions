class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS = {}
        seenT = {}

        for char in s:
            seenS[char] = seenS.get(char, 1) + 1

        for char in t:
            seenT[char] = seenT.get(char, 1) + 1

        if seenS == seenT:
            return True
        return False
        