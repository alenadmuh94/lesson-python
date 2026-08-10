def josephus_task(num_people, kill_num):
    """Задача Иосифа Флавия
    :param num_people: количество воинов
    :param kill_num: номер воина
    :return: номер последнего оставшегося воина
    """
    # todo Здесь нужно написать код

    # создаем список людей

    people = [i for i in range(1, num_people+1)]

    # цикл выполняем пока длинна списка не будет равна 1
    while len(people) > 1:
        # нужно чтобы необходимый элемент всегда был нулевым в списке,
        # а все элементы стоящие перед ним добавлялись в конец списка
        for i in range(kill_num-1):
            people.append(people[0])
            people.pop(0)
        people.pop(0)
    return people[0]


print(josephus_task(7, 3))
