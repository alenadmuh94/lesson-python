def create_phone_number(num_tuple):
    """Создание номера телефона
    :param num_tuple: кортеж из цифр
    :return: строку в виде номера телефона
    """
    # todo Здесь нужно написать код

    num_tuple_string = [str(i) for i in num_tuple]

    number_part_1 = "".join(num_tuple_string[:3])
    number_part_2 = "".join(num_tuple_string[3:6])
    number_part_3 = "".join(num_tuple_string[6:])

    return f'({number_part_1}) {number_part_2}-{number_part_3}'