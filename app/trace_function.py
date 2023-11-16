from requests_funcs import *
from inspect import signature

def trace_command(command_name: str):
    '''
        По запросу пользователя отыскивает нужную команду,
        если команда не найдена, возвращает сообщение о том, что это неизвестная команда
    '''
    return {"-get" : get_weather, 
            "-get_me" : get_weather_me, 
            "-history" : print_history,
            "-help" : helpFunction,
            "-exit" : breakFunction
           }.get(command_name, UNKNOWN)

def match_and_apply_function(input_line: str) -> str:
    '''
        Сопоставляет команду пользователя с командой в программе, вызывает ее
    '''
    splitted_input = input_line.split(" ")
    user_command = splitted_input[0]
    command = trace_command(user_command)
    if command != UNKNOWN:
        args_length = len(signature(command).parameters)
        is_enought_args = (len(splitted_input) - 1 >= args_length)
        if not args_length:
            return command()
        elif is_enought_args:
            return command(splitted_input[1])
        else:
            return NOT_ENOUGHT_ARGS_MSG
    else:
        return UNKNOWN_COMMAND_MSG