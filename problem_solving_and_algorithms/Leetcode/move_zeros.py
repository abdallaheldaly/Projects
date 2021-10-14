nums = [9, 2, 40, 0, 59, 63, 0, 7, 64, 15, 0]

print(nums)

nums.sort()
print(nums)

insert_index = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[insert_index] = nums[i]
        insert_index += 1
for i in range(insert_index,len(nums)):
    nums[i] = 0

print(nums)