def minimum_length_slice(first_string, second_string, therd=None):
    """Срез минимальной длины
    :param first_string: первая строка
    :param second_string: вторая строка
    :return: min_slice срез минимальной длины строки second_string
    """
    # todo Здесь нужно написать код
    first = second_string.find(first_string[0])
    second = second_string.find(first_string[1])
    third = second_string.find(first_string[2])

    min_slice = second_string[min(first, second, third): max(first, second, third)+1]
    return min_slice
