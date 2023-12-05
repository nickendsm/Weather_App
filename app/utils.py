from dataclasses import dataclass


APPID = "9acf9f262474a23f24d984f1298a3ec8"
WEATHER_SITE = "http://api.openweathermap.org/data/2.5/weather"
HISTORY_FILENAME = "history.txt"
SPLIT_SYMBOL = "*"
HELP_TEXT = "-get cityname - получение информации о погоде в городе cityname\n" \
            "-get_me - получение информации о погоде в городе, соответствующему вашему IP-адресу\n" \
            "-history n - получение информации по последним n запросам, выведенной построчно\n" \
            "-help - вывод информации о списке доступных пользователю команд\n" \
            "-exit - завершение работы программы"
START_MESSAGE = "Программа готова к работе"
CONTINUE = True
EXIT = False

@dataclass
class Weather:
    """
    Датакласс содержит данные о погоде, в частности:
    - Текущее время в населенном пункте
    - Имя населенного пункта
    - Сводка погоды
    - Температура воздуха по термометру
    - Температура воздуха по ощущениям
    - Скорость ветра

    """
    time: str
    place: str
    weather: str
    real_temperature: int
    feels_like_temparature: int
    wind_speed: float


    def __str__(self) -> str:
        """
        Формирует отчет, который будет показан пользователю
        """
        return f"Текущее время: {self.time}\n" \
            f"Название города: {self.place}\n" \
            f"Погодные условия: {self.weather}\n" \
            f"Текущая температура: {self.real_temperature} градусов по цельсию\n" \
            f"Ощущается как: {self.feels_like_temparature} градусов по цельсию\n" \
            f"Скорость ветра: {self.wind_speed} м/c"



def print_help_text() -> None:
    """
    Выводит пользователю информацию о доступных командах 
    """
    print(HELP_TEXT)