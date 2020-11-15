def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """


    nums1 = set(list(str(num1))) #convert num1 into a set of nums1
    nums2 = set(list(str(num2))) #convert num2 into a set of nums2

    num_count_dict1 = {}
    num_count_dict2 = {}

    if nums1 == nums2:
        #initialize two dictionaries for the two numbers
        num_count_dict1 = {}
        num_count_dict2 = {}

        # for first num, create a num count dictionary
        for num in nums1:
            if num in num_count_dict1:
                num_count_dict1[num] += 1
            else:
                num_count_dict1[num] = 1
        # for second num, create a num count dictionary
        for num in nums2:
            if num in num_count_dict2:
                num_count_dict2[num] += 1
            else:
                num_count_dict2[num] = 1
    else: 
        return False #if there aren't the same nums in both sets, return False
        
    return (num_count_dict1 == num_count_dict2) # if the two dictionaries are the same, the num counts are same
    



    # vowel_count_dict = {}
    # for letter in phrase:
    #     letter = letter.lower()
    #     if vowels.find(letter) >= 0:
    #         if letter in vowel_count_dict:
    #             vowel_count_dict[letter] += 1
    #         else:
    #             vowel_count_dict[letter] = 1
    
    # return vowel_count_dict


print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))

