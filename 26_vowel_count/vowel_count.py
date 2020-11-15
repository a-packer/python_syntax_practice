def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    vowel_count_dict = {}
    for letter in phrase:
        letter = letter.lower()
        if vowels.find(letter) >= 0:
            if letter in vowel_count_dict:
                vowel_count_dict[letter] += 1
            else:
                vowel_count_dict[letter] = 1
    
    return vowel_count_dict

# vowel_count('rithm school')
# vowel_count('HOW ARE YOU? i am great!')