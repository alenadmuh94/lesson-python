def to_roman(val):
    """Преобразование арабского числа в римское
    :param val: арабское число
    :return: римское число
    """
    # todo Здесь нужно написать код

    rim = {
        1000: "M", 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    roman_str = ''
    while val > 0:
        for i in rim.keys():
            roman_str += val // i * rim[i]
            val = val % i
    return roman_str
