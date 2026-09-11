class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        scanned_elements = set()

        for num in nums:
            if num in scanned_elements:
                return True
            else:
                scanned_elements.add(num)

        return False


        