from need_to_move import need_to_move
from is_cbs import is_cbs
from check_of_input import check_of_input


def main():
    print('Введите stop, чтоб завершить программу ')
    while (lisp_reference := input('Введите строку: ')) != 'stop':
        if check_of_input(lisp_reference):
            if is_cbs(lisp_reference):
                print('Это ПСП')
            else:
                print('Это не ПСП')
                if need_to_move(lisp_reference):
                    print('Количество символов, котторые нужно перенести: ', need_to_move(lisp_reference))
                else:
                    print('Нет символов которые возможно перенести')


if __name__ == '__main__':
    main()
