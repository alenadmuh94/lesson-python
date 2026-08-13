def scrabble(word):
    """Игра 'Эрудит'
    :param word: слово
    :return: количество очков за слово
    """
    # todo Здесь нужно написать код
    dct = {
        ('а', 'в', 'е', 'ё', 'и', 'н', 'о', 'р', 'с', 'т'): 1,
        ('д', 'к', 'л', 'м', 'п', 'у'): 2,
        ('б', 'г', 'ь', 'я'): 3,
        ('й', 'ы'): 4,
        ('ж', 'з', 'х', 'ц', 'ч'): 5,
        ('ф', 'ш', 'э', 'ю'): 8,
        ('щ',): 10,
        ('ъ',): 15
    }

    points = 0
    for letter in word:
        for key, value in dct.items():
            if letter in key:
                points += value
    return points


