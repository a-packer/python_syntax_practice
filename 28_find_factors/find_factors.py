def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    potential_factors = range(1,int(num/2)+1) # max factor is num/2


    factors = [factor for factor in potential_factors if num % factor == 0]
    factors.append(num) #include the num itself

    return factors


# print(find_factors(10))
# print(find_factors(111))
# print(find_factors(321421))
