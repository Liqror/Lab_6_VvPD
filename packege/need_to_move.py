def need_to_move(lisp_reference: str) -> int:
    """
    Функция находить количество изменений,
    чтобы получить ПСП из полученной строки

    Parameters
    ----------
    lisp_reference: str
        введенная пользователем, строка

    Returns
    -------
    result: int
        Возможные значения:
        0 - не возможно что-то переместить чтоб строка стала ПСП
        любое натуральное число - количество перемещений которые нужно совершить
    """
    count = 0
    result = 0
    for i in lisp_reference:
        if i == "(":
            count += 1
        else:
            count -= 1
        if abs(count) > result:
            result = abs(count)
    if count != 0:
        return 0
    else:
        return result
