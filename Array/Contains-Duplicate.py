def has_duplicates(nums):

    for num in nums:
        if nums.count(num) > 1:
            return True
    
    return False


nums = [9,3,4]
print(has_duplicates(nums))
