def multiplication_chain(num):
    """Цепочка умножений
    :param num: положительное число
    :return: количество перемножений
    """
    # todo Здесь нужно написать код
    count = 0
    while num >= 9:
        num_new = 1
        num = str(num)
        for i in num:
            num_new *= int(i)
        count += 1
        num = num_new
    return count
