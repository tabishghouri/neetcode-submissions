class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        # want to fill the res array with all left products except self
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        rightProduct = 1 # at 1 to keep it neutral, will be used to update res array
        
        # want to go backwards 
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= rightProduct

            # update rightProduct
            rightProduct *= nums[i]
        return res
            
        