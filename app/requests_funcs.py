import requests
import geocoder
from http import HTTPStatus
from custom_and_http_errors import HTTPError
from making_response_and_log import get_weather_and_write_in_history
from msges_and_consts import WEATHER_SITE, APPID


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
        weather = get_weather_and_write_in_history(request_json)
        print(weather)
    else:
        raise HTTPError(status)


def get_weather_me() -> None:
    """
        Взятие погоды по местоположению пользователя.
        Местоположение определяется по IP библиотекой geocoder.
        Вызывается функция get_weather, если удалось определить местоположение.
    """
    request = geocoder.ip("me")
    status = request.status_code
    city_and_country = request.city + ", " + request.country 
    if status == HTTPStatus.OK:
        get_weather_and_print(city_and_country)
    else:
        raise HTTPError(status)
