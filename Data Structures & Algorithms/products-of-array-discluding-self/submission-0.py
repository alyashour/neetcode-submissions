class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        out = []
        l = len(nums)

        # forward loop
        for n in nums[:-1]:
            prefix.append(prefix[-1] * n)
        
        # backwards loop
        for n in reversed(nums[1:]):
            suffix.append(suffix[-1] * n)
        
        # build out
        for i in range(l):
            p = prefix[i]
            s = suffix[l - i - 1]
            out.append(p * s)

        return out

