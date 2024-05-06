def has_duplicates(nums):
    counts_set = set()

    for num in nums:
        if num in counts_set:
            return True
        counts_set.add(num)
    
    return False


nums = [9,1,2,3,6,7,8,9]
print(has_duplicates(nums))
