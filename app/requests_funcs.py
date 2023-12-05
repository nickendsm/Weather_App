import requests
import geocoder
from http import HTTPStatus
from custom_errors import HTTPError
from weather_response_make import get_and_log_weather
from utils import WEATHER_SITE, APPID


def get_weather_and_print(city: str) -> None:
    """
        Основная функция взятия погоды по названию города.
        Отправляет запрос, проверяет статус на ошибку.
        После этого на выходе дает либо сообщение об ошибке, либо данные о погоде.
    """
    request_json = requests.get(
        WEATHER_SITE, 
        params={
            "q": city, 
            "units": "metric", 
            "lang": "ru", 
            "APPID": APPID
        }
    ).json()
    status = int(request_json["cod"])
    if status == HTTPStatus.OK:
        weather = get_and_log_weather(request_json)
        print(weather)
    else:
        raise HTTPError(status)


def get_location() -> tuple:
    request = geocoder.ip("me")
    status = request.status_code
    city = request.city
    return city, status


def get_weather_me() -> None:
    """
        Взятие погоды по местоположению пользователя.
        Местоположение определяется по IP библиотекой geocoder.
        Вызывается функция get_weather, если удалось определить местоположение.
    """
    city, status = get_location()
    if status == HTTPStatus.OK:
        get_weather_and_print(city)
    else:
        raise HTTPError(status)
