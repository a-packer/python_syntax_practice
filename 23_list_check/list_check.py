def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    response = True
    for item in lst:
        if not isinstance(item, list):
            response = False

    return response


# print(list_check([[1], [2, 3]]))
# print(list_check([[1], "nope"]))