def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    most_freq = 0
    freq_num = None
    for num in nums:
        frequency = nums.count(num)
        if frequency > most_freq:
            freq_num = num
    return freq_num    


