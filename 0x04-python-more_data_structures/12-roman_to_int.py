#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    conversion_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    num = 0
    i = 0
    str_len = len(roman_string)
    while i < str_len:
        current_digit = conversion_dict[roman_string[i]]
        if i + 1 < str_len:
            next_digit = conversion_dict[roman_string[i + 1]]
            if current_digit < next_digit:
                num += next_digit - current_digit
                i += 1
            else:
                num += conversion_dict[roman_string[i]]
        else:
            num += conversion_dict[roman_string[i]]
        i += 1
    return num
