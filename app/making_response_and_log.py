from help_and_history_funcs import opened_w_error
from dataclasses import dataclass
from msges_and_consts import SPLIT_SYMBOL, HISTORY_FILENAME
from custom_and_http_errors import FailedToOpenFile
from datetime import datetime, timezone, timedelta


def get_time(json_data: dict) -> datetime:
    """ 
    Функция, используемая для получения данных о времени и дате на основе json-ответа от сервера 
    """
    unix_timestamp = int(json_data["dt"])
    shift_from_UTC = int(json_data["timezone"])
    our_shift_hours = datetime.utcfromtimestamp(shift_from_UTC).hour
    our_shift_minutes = datetime.utcfromtimestamp(shift_from_UTC).minute
    our_time = datetime.fromtimestamp(
        unix_timestamp - shift_from_UTC,
        tz=timezone(timedelta(hours=our_shift_hours, minutes=our_shift_minutes)),
    )
    return our_time


@dataclass
class Weather:
    """
    Датакласс может содержать основную информацию о погоде:
    - Текущее время в населенном пункте
    - Имя населенного пункта
    - Сводка погоды
    - Температура воздуха по термометру
    - Температура воздуха по ощущениям
    - Скорость ветра

    """
    time : str
    place : str
    weather : str
    real_temperature : int
    feels_like_temparature : int
    wind_speed : float


    def __str__(self) -> str:
        """
        Генерирует отчет для пользователя о погоде,
        основываясь на записанных в поля сведениях
        """
      
        report = f"Текущее время: {self.time}\n" \
            f"Название города: {self.place}\n" \
            f"Погодные условия: {self.weather}\n" \
            f"Текущая температура: {self.real_temperature} градусов по цельсию\n" \
            f"Ощущается как: {self.feels_like_temparature} градусов по цельсию\n" \
            f"Скорость ветра: {self.wind_speed} м/c"
        return report


def get_weather_and_write_in_history(request: dict) -> Weather:
    """
    Функция, выводящая пользователю данные о погоде по текущему запросу и записывающая их в историю.
    Для записи в историю в конце вызывается функция write_in_history.
    """
    weather_info = Weather(
            time = get_time(request),
            place = request["name"],
            weather = request["weather"][0]["description"],
            real_temperature = int(request["main"]["temp"]),
            feels_like_temparature = int(request["main"]["feels_like"]),
            wind_speed = request["wind"]["speed"]
        )
    write_in_history(weather_info)
    return weather_info


def write_in_history(weather_info: str) -> None:
    """
    Непосредственно записывает данные по текущему запросу в историю.
    """
    report_info = str(weather_info) + "\n" + SPLIT_SYMBOL + "\n"
    with opened_w_error(HISTORY_FILENAME, mode="a") as (f, err):
        if err:
            raise FailedToOpenFile
        else:
            f.write(report_info)
