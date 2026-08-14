class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_dict = {}
        for index, number in enumerate(nums):
            complement = target - number

            if complement in num_dict:
                return [num_dict[complement], index]

            num_dict[number] = index

