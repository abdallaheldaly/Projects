class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len (nums)
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                 if target <= nums[high - 1] and target > nums[mid]:
                    low = mid + 1
                 else:
                    high = mid
        return -1
            

##########################

def binarySearchWhile(array, high, low,target):
    while high <= low:
        mid = high + (low - high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            high = mid + 1
        else :
            low = mid - 1
    return -1



def binarySearchIF (array, low, high, target): 
  
    if high >= low:
  
        mid = low + (high - low) // 2
  
        if array[mid] == target:
            return mid
          
        elif array[mid] > target:
            return binarySearchIF(array, low, mid -1, target)
  
        else:
            return binarySearchIF(array, mid +1, high, target)
  
    else:
        return -1


# Driver Code
array = [2, 4, 6, 7, 9, 26, 56, 33,63]
array.sort()
print(array)
target = 33

# Function call
result = binarySearchWhile(array, 0, len(array) -1, target)

result = binarySearchIF(array, 0, len(array)-1, target)


if result != -1:
    print(result)
else:
    print("Elament is not present in array")