class Solution:

    # can encode each letter with its number and a #
    # so ["Hello", "World"] will be encoded as:
    # 5#Hello5#World
    # decoder would read 5# and know the string is 5 chars long

    def encode(self, strs: List[str]) -> str:
        # want to get len of string and add that length with #
        return "".join(str(len(s)) + "#" + s for s in strs)

    def decode(self, s: str) -> List[str]:
        # now we want it to see 5# or something and understand the string is that long
        result = []
        i = 0 # start at beginning of string

        while i < len(s):
            # find where # is
            j = i
            while s[j] != "#":
                j += 1

            # so eventually i = 0 which is 5 and j = 1 which is #
            # then want to get the length which is everything between i and j
            # 123# -> s[i:j] = "123"
            length = int(s[i:j])

            # now need to figure out where the string starts and ends
            # move pointer past #
            i = j + 1

            # at this point i is at index of first letter of string
            # now want to extract the word from the first index to its length
            word = s[i : i + length]
            result.append(word)

            # move i to the next chunk
            # so itll move to 5#World
            i += length
        return result



