def max_division_by_3(num):
    """Преобразование числа
    :param num: натуральное число
    :return: другое натуральное число, удовлетворяющее условиям
    """
    # todo Здесь нужно написать код

    num_list = [i for i in str(num)]

    for idx, number in enumerate(num_list):
        for i in range(9, int(number), -1):
            num_list[idx] = str(i)
            summa = 0
            for j in num_list:
                summa += int(j)
            if summa % 3 == 0:
                s = int(''.join(num_list))
                return s
            else:
                num_list[idx] = number

