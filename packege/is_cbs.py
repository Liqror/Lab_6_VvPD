def is_cbs(lisp_reference: str) -> bool:
    """
    Проверяет является ли полученная строка ПСП

    Parameters
    ----------
    lisp_reference: str
        введенная пользователем, строка
    """
    count = 0
    for i in lisp_reference:
        if i == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    if count != 0:
        return False
    return True
