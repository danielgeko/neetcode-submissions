class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        i = 0
        num_dict = {}
        while i < len(nums):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = 1
            else:
                return True
            i += 1
        return False
