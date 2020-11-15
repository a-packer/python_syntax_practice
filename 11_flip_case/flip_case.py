def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase_list = []
    phrase_list = list(phrase)
    print(phrase_list)
    for letter in phrase_list:
        if letter.upper() == to_swap.upper():
            print("same")
            letter = letter.swapcase()
            new_phrase_list.append(letter)
        else:
            new_phrase_list.append(letter)
    new_phrase = "".join(new_phrase_list)
    
    print (new_phrase)

# test
# flip_case('Aaaahhh', 'a')