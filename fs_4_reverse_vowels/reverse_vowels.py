def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    char_list = list(s)

    i = 0
    vowels_i = []
    vowels = []

    for char in char_list:
        if char in 'aeiou':
            vowels_i.append(i)
            vowels.append(char)
            i += 1
        else:
            i += 1

    vowels.reverse() #reverse order of letters

    i = 0  #index for char_list
    j = 0  #index for vowels_i

    for char in char_list:
        if i in vowels_i:
            char_list[i] = vowels[j]
            j += 1 
        i +=1

    return ''.join(char_list)
         
     




# print(reverse_vowels("Hello!"))
# print(reverse_vowels("Tomatoes"))
# print( reverse_vowels("Reverse Vowels In A String"))
# print(reverse_vowels("aeiou"))
# print(reverse_vowels("why try, shy fly?"))
