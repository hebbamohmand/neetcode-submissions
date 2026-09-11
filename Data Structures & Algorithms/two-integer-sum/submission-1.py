class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        scanned_nums = {} # hashmappie, val: index

        for index, num in enumerate(nums):
            remainder = target - num
            if remainder in scanned_nums:
                return [scanned_nums[remainder], index]
            scanned_nums[num] = index
        return
        