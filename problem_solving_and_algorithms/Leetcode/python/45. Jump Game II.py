class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end = 0
        jumps = 0
        farthest = 0
        
        for i in range(len(nums)):
            farthest = max(farthest, nums[i] + i)
            
            if i == end and i != len(nums)-1:
                jumps+=1
                end = farthest
        return jumps
