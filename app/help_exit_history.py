import os
from errors_msges_other import *
from requests_funcs import *
from msges_and_consts import *
from contextlib import contextmanager


@contextmanager
def opened_w_error(filename: str, mode="r") -> None:
    '''
        Контекстный менеджер, обрабатывающий ошибки при открытии файла.
    '''
    try:
        f = open(filename, mode)
    except (IOError, Exception):
        yield None, Exception
    else:
        try:
            yield f, None
        finally:
            f.close()


def get_history_from_file(number: int) -> str:
    '''
        Непосредственно берет последние number записей из истории и передает функции print_history для вывода на экран
    '''
    with opened_w_error(HISTORY_FILENAME, mode="r") as (f, err):
            if err:
                return (HISTORY_ERROR_MSG, err)
            else:

                whole_history = f.read().split(SPLIT_SYMBOL + "\n")[::-1]
                del(whole_history[0])
                history_to_print = "\n".join(whole_history[:number])
                return history_to_print


def print_history(number: str) -> str:
    '''
        Проверяет, есть ли файл с историей и, в случае удачи, выводит историю, полученную 
        функцией get_history_from_file, на экран.
    '''
    try:
        number = int(number)
        if os.path.isfile(HISTORY_FILENAME):
            return get_history_from_file(number)
        else:
            return FILE_NOT_FOUND_MSG
    except Exception:
        return BAD_ARGS

def helpFunction() -> None:
    '''
        Выводит пользователю информацию о доступных командах
    '''
    return HELP_TEXT

def breakFunction() -> str:
    '''
        Нужна для того, чтобы обработать случай, когда пользователь хочет закрыть программу
        Возвращает флажок для вызова команды break в основном цикле программы
    '''
    return "break"
