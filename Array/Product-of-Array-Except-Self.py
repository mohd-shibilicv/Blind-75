def product_except_self_with_division(nums):
    # Compute the product of all elements in the array
    total_product = 1
    zero_count = 0
    for num in nums:
        if num != 0:
            total_product *= num
        else:
            zero_count += 1

    result = []
    for num in nums:
        if zero_count > 1:
            result.append(0)  # If more than one zero, all products except self are zero
        elif zero_count == 1:
            if num == 0:
                result.append(total_product)  # The product except self is total product of non-zero elements
            else:
                result.append(0)  # The product except self is zero if the element is non-zero
        else:
            result.append(total_product // num)  # No zeros in array
    return result


# Test the function
nums = [1, 2, 3, 4]
print(product_except_self_with_division(nums))

nums_with_zero = [1, 2, 0, 4]
print(product_except_self_with_division(nums_with_zero))

nums_with_two_zeros = [1, 0, 3, 0]
print(product_except_self_with_division(nums_with_two_zeros))
