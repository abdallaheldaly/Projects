class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        arr = nums
        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if lo == hi:
                return arr[lo]
            if arr[0] < arr[mid] < arr[hi]:
                return arr[0]
            if arr[mid - 1] > arr[mid] and arr[mid] < arr[mid + 1]:
                return arr[mid]
            else:
                if arr[mid] > arr[hi] :
                    lo = mid + 1
                else:
                    hi = mid - 1  
                    
                    
                    
