import requests
import geocoder
from error_msges_http import *
from making_response_and_log import *


def exception(status: int) -> str:
    '''
        Функция, обрабатывающая ошибки обращения к серверу.
    '''
    if status in ERRORS_HTTP:
        return ERRORS_HTTP[status]
    return f"Ошибка с кодом {status}"


def get_weather(city: str) -> str:
    '''
        Основная функция взятия погоды по названию города.
        Отправляет запрос, проверяет статус на ошибку.
        После этого на выходе дает либо сообщение об ошибке, либо данные о погоде.
    '''
    request_json = requests.get(WEATHER_SITE, 
                           params={"q": city, 
                                   "units": "metric", 
                                   "lang": "ru", 
                                   "APPID": APPID}).json()
    status = int(request_json["cod"])
    if status == HTTPStatus.OK:
        return print_weather_and_write_in_history(request_json)
    else:
        return exception(status)

def get_weather_me() -> str:
    '''
        Взятие погоды по местоположению пользователя.
        Местоположение определяется по IP библиотекой geocoder.
        Вызывается функция get_weather, если удалось определить местоположение.
    '''
    request = geocoder.ip("me")
    city_and_country = request.city + ", " + request.country 
    return get_weather(city_and_country) if (request.status_code == HTTPStatus.OK) else exception(request)