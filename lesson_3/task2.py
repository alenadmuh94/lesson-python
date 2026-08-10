def get_list_info(lst):
    """Получение информации о списке
    :param lst: список из чисел
    :return: min_elem, max_elem, sum_list, average
    """
    # todo Здесь нужно написать код
    lst_new = []
    lst_new.extend([min(lst), max(lst), sum(lst), round(sum(lst)/len(lst), 2)])
    lst_new = tuple(lst_new)
    return lst_new

