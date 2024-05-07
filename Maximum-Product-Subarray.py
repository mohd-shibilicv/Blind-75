def max_product(nums):
    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        max_prod = max(num, max_prod * num, min_prod * num)
        min_prod = min(num, max_prod * num, min_prod * num)
        result = max(result, max_prod)
    
    return result


nums = [2,3,-2,4]
max_product_value = max_product(nums)
print(max_product_value)
