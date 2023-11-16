from datetime import datetime, timezone, timedelta
from help_exit_history import *


def get_time(json_data: dict) -> datetime:
    '''
        Функция, используемая для получения данных о времени и дате на основе json-ответа от сервера.
    '''
    shift_from_UTC = int(json_data["timezone"])
    tz = timezone(timedelta(seconds=shift_from_UTC))
    return datetime.now(tz=tz)


def print_weather_and_write_in_history(request: dict) -> str:
    '''
        Функция, выводящая пользователю данные о погоде по текущему запросу и записывающая их в историю.
        Для записи в историю в конце вызывается функция write_in_history.
    '''
    date_and_time = get_time(request)
    city_name = request["name"]
    weather = request["weather"][0]["description"]
    temperature = int(request["main"]["temp"])
    temperature_like = int(request["main"]["feels_like"])
    wind_speed = request["wind"]["speed"]
    weather_info = f"Текущее время: {date_and_time}\n"\
            f"Название города: {city_name}\n"\
            f"Погодные условия: {weather}\n"\
            f"Текущая температура: {temperature} градусов по цельсию\n"\
            f"Ощущается как: {temperature_like} градусов по цельсию\n"\
            f"Скорость ветра: {wind_speed} м/с"

    write_in_history(weather_info)
    return weather_info


def write_in_history(weather_info: str) -> None:
    '''
        Непосредственно записывает данные по текущему запросу в историю.
    '''
    report_info = weather_info + "\n" + SPLIT_SYMBOL + "\n"
    with opened_w_error(HISTORY_FILENAME, mode="a") as (f, err):
        if err:
            print(WRITE_ERROR_MSG, err)
        else:
            f.write(report_info)
