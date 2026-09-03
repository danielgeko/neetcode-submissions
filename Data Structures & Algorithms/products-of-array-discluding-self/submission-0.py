class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        l_mult = 1
        r_mult = 1

        prefix, postfix = [1] * n, [1] * n
        for i in range(n):
            j = -i -1
            prefix[i] = l_mult
            postfix[j] = r_mult

            l_mult *= nums[i]
            r_mult *= nums[j]
        

        return [l*r for l, r in zip(prefix, postfix)]

            
            






        