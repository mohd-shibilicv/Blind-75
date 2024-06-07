def two_sum(nums: list[int], target: int) -> (list | None):
    # Initialize a dictionary to store the complements of the elements in `nums` array
    complements_dict = {}

    # Iterate over the nums array to find complement of each element in the `nums` array
    for i, num in enumerate(nums):
        # Find the complement of `target` value and the current element
        complement = target - num
        # Check if the complements is in the complements dict,
        # if yes, that means the current element can add up to the target
        if complement in complements_dict:
            # Return the current index and the index of the complement element
            return [i, complements_dict[complement]]
        # If the complement is not in the complements dict,
        # add the array element to the dict with the index as it's value
        complements_dict[num] = i

    # If no elements in the nums array add up to the target, return None or a empty list
    return None


nums = [1, 2, 3, 4, 5, 6, 7, 8]
target = 9
print(two_sum(nums, target))
