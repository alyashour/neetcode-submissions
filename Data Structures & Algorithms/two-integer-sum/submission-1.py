class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for idx in range(len(nums)):
            val = nums[idx]
            diff = target - val
            if diff in h:
                return [h[diff], idx]
            
            h[val] = idx
        
        return []

