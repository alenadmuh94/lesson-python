def modification(lst):
    """Изменение списка
    :param lst: список
    :return: преобразованный список
    """
    # todo Здесь нужно написать код
    first_elem_list = lst[0]
    second_elem_list = lst[-1]
    lst[0] = second_elem_list
    lst[-1] = first_elem_list
    return lst
