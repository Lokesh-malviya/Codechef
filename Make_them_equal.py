class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_ending_here = 0
     
        for i in range(0, len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if max_ending_here < 0:
                max_ending_here = 0
            elif (max_so_far < max_ending_here):
                max_so_far = max_ending_here
             
        return max_so_far

