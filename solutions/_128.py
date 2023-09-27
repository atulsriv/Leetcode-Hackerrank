class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_cache = set(nums)
        max_length = 1 if len(nums) >= 1 else 0

        for n in nums:
            if n - 1 not in num_cache:
                length = 0
                # start of a sequence
                while (n + length) in num_cache:
                    length += 1
                max_length = max(length, max_length)

        return max_length