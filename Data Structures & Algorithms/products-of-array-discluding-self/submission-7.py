class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixes = [1]
        out = []
        
        # backwards loop
        s = 1
        # skip i == 0, count backwards
        for i in range(len(nums) - 1, 0, -1): 
            n = nums[i]
            s *= n
            suffixes.append(s)

        # forward loop
        p = 1
        for i, n in enumerate(nums): # loop forwards
            out.append(p * suffixes[len(nums) - 1 - i])
            p *= n

        return out

