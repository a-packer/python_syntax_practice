def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_dict = {}
    each_letter = set(phrase)
    phrase_list = list(phrase)
    for letter in each_letter:
        letter_count = phrase_list.count(letter)
        letter_dict[letter] = letter_count
    return(letter_dict)
