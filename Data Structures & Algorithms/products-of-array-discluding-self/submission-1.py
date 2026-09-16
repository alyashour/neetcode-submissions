class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixes = [1]
        out = []
        l = len(nums)
        
        # backwards loop
        for i in range(l - 1, 0, -1):
            n = nums[i]
            suffixes.append(suffixes[-1] * n)

        # forward loop
        p = 1
        for i, n in enumerate(nums):
            # find out
            s = suffixes[l - i - 1]
            out.append(p * s)

            # uptick prefix
            p *= n

        return out

