class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
#         i = len(nums) - 2
#         while not (i < 0 or nums[i] < nums[i + 1]):
#             i -= 1
#         if i < 0:
#             return False
#         j = len(nums) - 1
        
#         while not (nums[j] > nums[i]):
#             j -= 1
#         nums[i], nums[j] = nums[j], nums[i]
#         nums[i + 1 : ] = reversed(nums[i + 1 : ])  
#         return True



        n = len(nums)
 
        if n < 2 :
            return nums
 
        inverse = -1
        i = n - 2
 
        while i >= 0 :
            if nums[i] < nums[i + 1]:
                inverse = i
                break
            i -= 1
        
        if inverse < 0 :
            nums.sort()
            i = 0
            while nums[i] == 0 :
                i += 1
            if i != 0 :
                nums[0], nums[i] = nums[i], nums[0]
            return nums
 
        i = n-1
 
        while i >= 0 :
            if nums[inverse] < nums[i] :
                nums[inverse], nums[i] = nums[i], nums[inverse]
                break
            i -= 1
        
        nums[inverse+1:] = reversed(nums[inverse+1:])
        return nums
