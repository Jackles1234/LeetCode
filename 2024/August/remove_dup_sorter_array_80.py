def removeDuplicates(nums):
    count = 0
    occurrence = 1
    while count < len(nums) - 1:
        if nums[count] == nums[count + 1]:
            occurrence += 1
            if occurrence >= 3:
                nums.pop(count + 1)
            else:
                count += 1
        else:
            occurrence = 1
            count += 1 
    return nums

print(removeDuplicates([1, 1, 1, 2, 2, 3]))
