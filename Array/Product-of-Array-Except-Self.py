def product_except_self(nums):
    n = len(nums)
    prefix_products = [1] * n
    suffix_prodcuts = [1] * n

    for i in range(1, n):
        prefix_products[i] = prefix_products[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        suffix_prodcuts[i] = suffix_prodcuts[i + 1] * nums[i + 1]

    result = [prefix_products[i] * suffix_prodcuts[i] for i in range(n)]

    return result


nums = [1, 2, 3, 4]
print(product_except_self(nums))
