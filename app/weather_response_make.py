from datetime import datetime, timezone, timedelta
from history_funcs import write_in_history
from utils import Weather


def get_time(json_data: dict) -> datetime:
    """ 
    Функция, используемая для получения данных о времени и дате на основе json-ответа от сервера 
    """
    unix_timestamp = int(json_data["dt"])
    shift_from_UTC = int(json_data["timezone"])
    tz = timezone(timedelta(seconds=shift_from_UTC))
    date = datetime.fromtimestamp(unix_timestamp, tz)
    return date


def get_and_log_weather(request: dict) -> Weather:
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
