def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    pair = ()

    for num in nums:
        curr_index = nums.index(num) # get current index and 
        next_index = curr_index + 1
        next_next_index = next_index + 1

        if curr_index < len(nums) -2:
            if (num + nums[next_index]) == goal:
                pair = (num, nums[next_index])
            elif (num + nums[next_next_index]) == goal:
                pair = (num, nums[next_index + 1])
    return pair

# print(sum_pairs([1, 2, 2, 10], 4))
# print(sum_pairs([4, 2, 10, 5, 1], 6)) # (4, 2)
# print(sum_pairs([5, 1, 4, 8, 3, 2], 7))
# print(sum_pairs([11, 20, 4, 2, 1, 5], 100))