def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    sentence_list = phrase.split(" ") #split sentence into list of words (or one word)
    word_list = list(sentence_list[0]) #split first word into a list of letters
    cap_letter = word_list[0].swapcase()
    word_list[0] = cap_letter
    cap_word = "".join(word_list)
    sentence_list[0] = cap_word
    return " ".join(sentence_list)
    

capitalize('python')
capitalize('only first word')