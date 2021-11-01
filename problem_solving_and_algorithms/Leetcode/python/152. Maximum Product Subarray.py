class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        max_list = [0] * len(nums)
        min_list = [0] * len(nums)
        max_list[0] = nums[0]
        min_list[0] = nums[0]
        
        for i in range(1, len(nums)):
            max_list[i] = max(max(max_list[i - 1] * nums[i], min_list[i - 1] * nums[i]), nums[i])
            min_list[i] = min(min(min_list[i - 1] * nums[i], nums[i]), max_list[i - 1] * nums[i])
            
        return max(max_list)
    
    
