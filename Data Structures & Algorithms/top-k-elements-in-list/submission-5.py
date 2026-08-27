class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # value is the count of how many times that number is there 
        for key, value in count.items():
            freq[value].append(key)

        result = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

'''
nums = [1,1,1,2,2,3]
k = 2

after going through the count for loop:
count = {
    1: 3,
    2: 2,
    3: 1
}

after going through the second for loop for adding it to the freq list:
freq = [
    [],
    [3],
    [2],
    [1],
    [],
    [],
    []
]

then in the third for loop we are starting from the end and moving backwards
eventually we'll hitL
i = 3
freq[3] = [1]

then we append this num to result so:
result = [1]

i = 2
freq[2] = [2]

result = [1, 2]

the len of result is == k so return result
'''      
