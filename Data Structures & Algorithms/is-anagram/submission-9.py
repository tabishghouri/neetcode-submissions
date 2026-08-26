class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # want to count freq of each letter
        # use a dict

        # first lets just get the count of each letter in each string
        countS = {}
        for char in s:
            countS[char] = countS.get(char, 0) + 1
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1

        # now want to see if counts of each letter are equal
        return countS == countT
        

        


