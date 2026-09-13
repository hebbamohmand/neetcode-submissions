class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1 #update count

        sorted_nums = sorted(
            count.keys(),
            key=lambda num: count[num],
            reverse=True #largest first
        )

        return sorted_nums[0:k]