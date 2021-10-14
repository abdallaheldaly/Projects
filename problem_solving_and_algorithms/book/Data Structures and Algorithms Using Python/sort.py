random = [(2, 2), (3, 4), (4, 1), (1, 3), (1, 2)]

# sort list with key
random.sort()

# print list
print( random)

###############
def binarySearch (array, low, high, target): 
  
    if high >= low:
  
        mid = low + (high - low) // 2
  
        if array[mid] == target:
            return mid
          
        elif array[mid] > target:
            return binarySearch(array, low, mid -1, target)
  
        else:
            return binarySearch(array, mid +1, high, target)
  
    else:
        return -1
  
# Driver Code
# Function call


array = [2, 3, 4, 10, 40]
target = 10

# Function call

result = binarySearch(array, 0, len(array)-1, target)
  
if result == -1:
    print ("Element is not present in array")
else:
    print ("Element is present at index ", result)

##################
def binarySearch(array, high, low, target):
      
    while high <= low:
  
        mid = high + (low - high) // 2
          
        if array[mid] == target:
            return mid
  
        elif array[mid] < target:
            high = mid + 1
  
        else:
            low = mid - 1
      
    return -1
  
array = [ 2, 3, 4, 10, 40 ]
target = 40
  
result = binarySearch(array, 0, len(array)-1, target)
  
if result != -1:
    print ("Element is present at index ", result)
else:
    print ("Element is not present in array")