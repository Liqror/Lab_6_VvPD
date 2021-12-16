def check_of_input(lisp_reference: str) -> bool:
    """
    Проверяем то ли пользователь ввел, а то программа дальше работать не будет

    Parameters
    ----------
    lisp_reference: str
        введенная пользователем, строка
    """
    allowable_values = {'(', ')'}
    for i in lisp_reference:
        if i not in allowable_values:
            return False
    return True
