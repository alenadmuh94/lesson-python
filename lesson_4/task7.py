def move_zeros(lst):
    """Перемещение нулей
    :param lst: список из цифр
    :return: список из цифр с нулями в конце
    """
    # todo Здесь нужно написать код

    count = lst.count(0)
    lst_without_zeros = [i for i in lst if i != 0]
    lst = lst_without_zeros + [0] * count
    return lst
