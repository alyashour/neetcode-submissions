class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixes = [1]
        out = []
        l = len(nums) - 1
        
        # backwards loop
        s = 1
        for i in range(l, 0, -1):
            n = nums[i]
            s *= n
            suffixes.append(s)

        # forward loop
        p = 1
        for i, n in enumerate(nums):
            # find out
            s = suffixes[l - i]
            out.append(p * s)

            # uptick prefix
            p *= n

        return out

