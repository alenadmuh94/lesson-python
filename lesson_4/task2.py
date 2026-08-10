def flatten_and_sort(array):
    """Преобразование двумерного массива в плоский список
    :param array: двумерный массив
    :return: плоский список
    """
    # todo Здесь нужно написать код

    list_new = []
    for i in array:
        for j in i:
            list_new.append(j)
    list_new.sort()
    return list_new
