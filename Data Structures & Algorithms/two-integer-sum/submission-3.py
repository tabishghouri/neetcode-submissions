class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # thinking of using sliding window for this
        # basically have a window of two int
        # add them and see if they equual target

        # after writing that im thinking of using the complement
        # basically do the target - first index value
        # then find the position of that in the array
        # if its not there than use the next number but make sure not to reuse
        # making sure not to reuse makes me think of hashmap/dict

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            # want to see if complement is in the dict
            # if not in there add the number that was used to get complement in the dict
            if complement in seen:
                return [seen[complement], i] 
            else:
                seen[num] = i
                
