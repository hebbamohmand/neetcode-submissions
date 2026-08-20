class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left = 1

        # calc products to left
        for i in range(len(nums)):
            output[i] = left
            left *= nums[i]

        right = 1

        # multiply products of left with products to right
        for i in range(len(nums) - 1, -1, -1): # loop moving to the left, starts from index 3, index, stop, step
            output[i] *= right
            right *= nums[i]
        
        return output
        