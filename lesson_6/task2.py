def global_function():
    """Нелокальные изменения
    :return: msg
    """
    msg = 1

        # todo Здесь нужно написать код
    def local_function():
        nonlocal msg
        msg = 2
        return msg

    local_function()

    return msg
