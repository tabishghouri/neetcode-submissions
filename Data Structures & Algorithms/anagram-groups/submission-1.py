class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # get freq of each letter for each letter and store in dict
        # compare the freq
        # when freq matches thats an anagram
        # return the grouped list from there

        # instead of getting freq, instead sort each word
        groups = {}

        for char in strs:
            sorted_words = "".join(sorted(char)) # so output is from ['a', 'c', 't'] to act
            if sorted_words in groups:
                # want to add the original
                # so 'act' 'act' would be added together in their original format of 'act' 'cat'
                groups[sorted_words].append(char)
                '''
                groups = {
                    "act" : ["act", "cat"]
                }
                '''
            else:
                groups[sorted_words] = [char]
                '''
                after first pass
                groups = {
                    "act":["act"]
                }
                '''
        return list(groups.values())

