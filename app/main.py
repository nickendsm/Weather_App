from utils import START_MESSAGE
from custom_errors import MyError
from trace_and_apply_funcs import execute_command


def main():
    """
    Основная функция, осуществляющая взаимодействие пользователя в бесконечном цикле
    Выход из функции происходит при вводе пользователем специальной команды
    """
    print(START_MESSAGE)
    flag = 1
    while(flag):
        try:
            input_command = input().strip().lower().split(" ")
            flag = execute_command(input_command)
        except MyError as error:
            print(error.message)
        except Exception as error:
            print(error)
        continue


if __name__ == "__main__":
    main()
