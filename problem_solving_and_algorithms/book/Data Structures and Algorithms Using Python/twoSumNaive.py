

def twoSumHashing(num_arr, pair_sum):
    sums = []
    hashTable = {}

    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
            print("Pair with sum", pair_sum,"is: (", num_arr[i],",",complement,")")
        hashTable[num_arr[i]] = num_arr[i]

# Driver Code
num_arr = [4, 5, 1, 8]
pair_sum = 5
  
# Calling function
twoSumHashing(num_arr, pair_sum)



# # Driver Code
# num_arr = [3, 5, 2, -4, 8, 11]
# pair_sum = 7

# def twoSumNaive(num_arr, pair_sum):
#       # search first element in the array
#     for i in range(len(num_arr) - 1):
#         # search other element in the array
#         for j in range(i + 1, len(num_arr)):
#             # if these two elemets sum to pair_sum, print the pair
#             if num_arr[i] + num_arr[j] == pair_sum:
#                 print("Pair with sum", pair_sum,"is: (", num_arr[i],",",num_arr[j],")")

# # Function call inside print
# twoSumNaive(num_arr, pair_sum)