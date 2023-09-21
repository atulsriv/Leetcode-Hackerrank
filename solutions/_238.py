from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret_arr = [1] * len(nums)

        prefix = 1
        postfix = 1

        for i in range(1, len(nums)):
            prefix = prefix * nums[i-1]
            ret_arr[i] *= prefix

        for i in range(len(nums)- 2, -1, -1):
            postfix = postfix * nums[i+1]
            ret_arr[i] *= postfix

        return ret_arr