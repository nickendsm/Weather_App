import os
from custom_errors import FileNotFound, BadArgs
from utils import HISTORY_FILENAME, SPLIT_SYMBOL, Weather


def get_history_from_file(number: int) -> str:
    """
    Непосредственно берет последние number записей из истории 
    и передает функции print_history для вывода на экран 
    """
    with open(HISTORY_FILENAME, mode="r") as f:
        whole_history = f.read().split(SPLIT_SYMBOL + "\n")[::-1]
        history_to_print = "\n".join(whole_history[1:number+1])
        return history_to_print


def print_history(number: int) -> None:
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


def write_in_history(weather_info: Weather) -> None:
    """
    Непосредственно записывает данные по текущему запросу в историю.
    """
    report_info = str(weather_info) + "\n" + SPLIT_SYMBOL + "\n"
    with open(HISTORY_FILENAME, mode="a") as f:
        f.write(report_info)
