def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """

    print(f"end is {end}")
    sum = 0
    if end and end <= len(nums):
        for num in nums[start:(end+1)]: #add one to end to include the ending num
            sum += num
    elif end:
        for num in nums[start:]:
            sum += num
    else:
        for num in nums[start:]:
            sum += num

    return sum


nums = [1, 2, 3, 4]
print(sum_range(nums))
print(sum_range(nums, 1))
print(sum_range(nums, end=2))
print(sum_range(nums, 1, 3))
print(sum_range(nums, 1, 99))