class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        S = set(nums)
 
        maxlength = 0
 
        for e in nums:
            if (e - 1) not in S:
 
                len = 1
    
                while (e + len) in S:
                    len += 1
                
                maxlength = max(maxlength, len)
 
        return maxlength

