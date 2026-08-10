def which_triangle(a, b, c):
    """Определение типа треугольника
    :param a: длина стороны
    :param b: длина стороны
    :param c: длина стороны
    :return: тип треугольника
    """
    # todo Здесь нужно написать код

    flag = ''
    if a < b+c and b < a+c and c < b+a:
        if a == b == c:
            flag = 'Равносторонний'
        elif a == b != c or b == c != a or c == a != b:
            flag = 'Равнобедренный'
        elif a != b != c:
            flag = 'Обычный'
    else:
        flag = 'Не треугольник'
    return flag

