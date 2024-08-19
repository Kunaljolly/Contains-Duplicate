class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        t = set(nums)
        if len(t) == len(nums):
            return False
        return True
       
