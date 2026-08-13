def letter_stat(our_str):
    """Буквенная статистика
    :param our_str: строка
    :return: словарь со статистикой по буквам
    """
    # todo Здесь нужно написать код
    letters_dict = dict()
    for letter in our_str:
        letters_dict[letter] = our_str.count(letter)
    return letters_dict


print(letter_stat('letter'))