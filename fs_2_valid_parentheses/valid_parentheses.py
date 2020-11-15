def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    parens_list = list(parens) #convert into a list of parens

    if len(parens) % 2 != 0: #if there isn't an even num of parens, invalid
        return False

    left = 0
    right = 0

    if parens_list[0] != '(' or parens_list[-1] != ')': #if it doesn't start with ( or end with ), invalid
        return False

    for paren in parens_list: #check to see if same num of '(' and ')'
        if paren == '(':
            left += 1
        elif paren == ')':
            right += 1
        else: 
            return False
    
    return left == right

        


    
# print(valid_parentheses("()"))
# print(valid_parentheses("()()"))
# print(valid_parentheses("(()())"))
# print(valid_parentheses(")()"))
# print(valid_parentheses("())"))
# print(valid_parentheses("((())"))
# print(valid_parentheses(")()("))

