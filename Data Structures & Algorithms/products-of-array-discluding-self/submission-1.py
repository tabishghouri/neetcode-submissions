class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        leftRes = [1] * len(nums)
        for i in range(1, len(nums)):
            leftRes[i] = leftRes[i - 1] * nums[i - 1]

        rightRes = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            rightRes[i] = rightRes[i + 1] * nums[i + 1]
        
        res = []
        for i in range(len(nums)):
            res.append(leftRes[i] * rightRes[i])
        
        return res
            
        