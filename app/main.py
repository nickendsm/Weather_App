from msges_and_consts import START_MESSAGE
from trace_and_apply_funcs import applying_function


def main():
    """
    Основная функция, осуществляющая взаимодействие пользователя в бесконечном цикле
    Выход из функции происходит при вводе пользователем специальной команды
    """
    print(START_MESSAGE)
    flag = 1
    while(flag):
        try:
            input_command = input().strip().lower()
            flag = applying_function(input_command)
        except Exception as error:
             print(error.message)
             continue


if __name__ == "__main__":
    main()
