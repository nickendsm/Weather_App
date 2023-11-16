from trace_function import *

def main():
    '''
        Основная функция, осуществляющая взаимодействие пользователя в бесконечном цикле
        Выход из функции происходит при вводе пользователем специальной команды
    '''
    print(START_MESSAGE)
    while(True):
        try:
            input_command = input().strip().lower()
            result = match_and_apply_function(input_command)
            if result == "break":
                break
            print(result)
        except Exception:
            print(UNKNOWN_ERROR)
            continue


if __name__ == "__main__":
    main()
