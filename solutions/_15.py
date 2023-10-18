class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []

        trips = []
        nums.sort()

        for i in range(0, len(nums) - 2):
            target = -nums[i]
            print(target)
            left = i + 1
            right = len(nums) - 1

            while left < right:
                inner_sum = nums[left] + nums[right]

                if inner_sum == target:
                    ret = [nums[i], nums[left], nums[right]]
                    if ret not in trips:
                        trips.append(ret)
                    left += 1

                elif inner_sum < target:
                    left += 1
                else:
                    right -= 1

        return trips
