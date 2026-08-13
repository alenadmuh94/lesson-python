def repeats(our_str):
    """Повторы букв
    :param our_str: строка
    :return: новая строка с повторами букв
    """
    # todo Здесь нужно написать код

    lib = dict.fromkeys([letter for letter in our_str], 0)
    string = ''
    for key in our_str:
        lib[key] += 1
        string += str(key) + '_' + str(lib[key])
    return string
