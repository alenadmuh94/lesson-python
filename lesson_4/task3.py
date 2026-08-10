def sum_digits(num: object) -> object:
    """Нахождение суммы цифр числа
    :param num: число
    :return: сумма цифр числа
    """
    # todo Здесь нужно написать код

    lst = str(num)
    sum_elem = 0
    for number in lst:
        sum_elem += int(number)

    return sum_elem


num = 39
print(sum_digits(num))
