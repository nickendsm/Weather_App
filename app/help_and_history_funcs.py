import os
from contextlib import contextmanager
from custom_and_http_errors import FailedToOpenFile, FileNotFound, BadArgs
from msges_and_consts import HISTORY_FILENAME, SPLIT_SYMBOL, HELP_TEXT


@contextmanager
def opened_w_error(filename: str, mode="r") -> None:
    """ 
    Контекстный менеджер, обрабатывающий ошибки при открытии файла
    """
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
    """
    Непосредственно берет последние number записей из истории 
    и передает функции print_history для вывода на экран 
    """
    with opened_w_error(HISTORY_FILENAME, mode="r") as (f, err):
            if err:
                raise FailedToOpenFile
            else:
                whole_history = f.read().split(SPLIT_SYMBOL + "\n")[::-1]
                history_to_print = "\n".join(whole_history[1:number+1])
                return history_to_print


def get_and_print_history(number: int) -> str:
    """
    Проверяет, есть ли файл с историей и, в случае удачи, выводит историю, полученную 
    функцией get_history_from_file, на экран.
    """
    if number < 0:
        raise BadArgs
    
    if os.path.isfile(HISTORY_FILENAME):
        history = get_history_from_file(number)
        print(history)
    else:
        raise FileNotFound


def print_help_text() -> None:
    """
    Выводит пользователю информацию о доступных командах 
    """
    print(HELP_TEXT)
