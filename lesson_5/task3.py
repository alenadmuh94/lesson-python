def everything_for_your_cat(cats_data):
    """Котики и их владельцы
    :param cats_data: информация о котах и их владельцах
    :return: информация о котах и их владельцах в виде строки
    """
    # todo Здесь нужно написать код

    dct = {}
    s = ''
    for tpl in cats_data:
        cat, age, name, surname = tpl
        print(cat, age)
        cat_info = f'{cat}, {age}'
        owner = f'{name} {surname}'
        if owner in dct:
            dct[owner] += f'; {cat_info}'
        else:
            dct[owner] = cat_info
    for key, value in dct.items():
        s += f'{key}: {value}\n'
    return s


