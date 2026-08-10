def string_concatenation(str1, str2):
    """Объединение строк
    :param str1: первая строка
    :param str2: вторая строка
    :return: преобразованную строку
    """

    # todo Здесь нужно написать код
    str1_new = str2[:2] + str1[2:]
    str2_new = str1[:2] + str2[2:]
    result_string = str1_new + ' ' + str2_new
    return result_string
