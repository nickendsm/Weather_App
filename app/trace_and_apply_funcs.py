from enum import StrEnum
from help_and_history_funcs import get_and_print_history, print_help_text
from requests_funcs import get_weather_and_print, get_weather_me
from custom_and_http_errors import BadArgs, UnknownCommand
from msges_and_consts import CONTINUE, EXIT


class Command(StrEnum):
    GET_WEATHER_BY_CITY = "-get"
    GET_WEATHER_OF_MINE = "-get_me"
    HISTORY             = "-history"
    HELP                = "-help"
    EXIT                = "-exit"
    UNKNOWN             = "unknown"


def trace_command(command: Command) -> tuple:
    """
    По запросу пользователя отыскивает нужную команду,
    если команда не найдена, возвращает сообщение о том, что это неизвестная команда
    """
    return {
        Command.GET_WEATHER_BY_CITY: (get_weather_and_print, str), 
        Command.GET_WEATHER_OF_MINE: (get_weather_me, None), 
        Command.HISTORY: (get_and_print_history, int),
        Command.HELP: (print_help_text, None),
        Command.EXIT: (0, None)
    }.get(command, Command.UNKNOWN)


def parse_args(args: list, types: tuple) -> list:
    """
    Парсит аргументы, поданые пользователем, в нужный для работы функции тип
    """
    parsed_args = []
    try:
        for i in range(len(types)):
            parsed_args.append(types[i](args[i]))
        return parsed_args
    except Exception:
         raise BadArgs


def identify_command_and_args(splitted_input: list) -> tuple:
    """
    Отсекает от пользовательского ввода название команды, 
    с помощью функции trace_command сопоставляет названию команду программы
    """
    try:
        command = Command(splitted_input[0])
        action_and_types = trace_command(command)
        return action_and_types
    except Exception:
        raise UnknownCommand
    
def applying_function(input_line: str) -> bool:
    """
    Сопоставляет команду пользователя с командой в программе, вызывает ее
    Возвращает bool-значение как флаг, завершить работу программы или нет
    """
    splitted_input = input_line.split(" ")
    action_and_types = identify_command_and_args(splitted_input)
    action = action_and_types[0]
    match action:
        case 0:
            return EXIT
        case _:
            types_needed = action_and_types[1:]
            args = splitted_input[1:]
            if types_needed[0] != None:
                parsed_args = parse_args(args, types_needed)
                try:
                    action(*parsed_args)
                except TypeError:
                    raise BadArgs
            else:
                action()
    return CONTINUE
