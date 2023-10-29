# Weather_App
Консольное приложение, позволяющее получить информацию о погоде в городе, соответствующему местоположению пользователя (по IP), а также в любом другом по запросу.
## Подробности реализации
1) Получение информации по конкретному городу происходит с помощью метода get библиотеки [requests](https://requests.readthedocs.io/en/latest/user/quickstart/). Источник данных о погоде: https://openweathermap.org/
2) Определение текущей локации реализуется с помощью библиотеки [geocoder](https://pypi.org/project/geocoder/). Строка, содержащая текущий город и страну в качестве параметра передается в get-запрос.
3) История результатов запросов хранится в формате json-файле и выводится пользователю построчно в консоли.
4) Взаимодействие пользователя с программой происходит через консоль. Доступные пользователю команды:
*  `get cityname` - получение информации о погоде в городе cityname. Можно уточнить запрос, после запятой добавив информацию о стране, например:  `get cityname, country`, где country - сокращенное или полное название страны;
*  `-get_me` - получение информации о погоде в городе, соответствующему вашему IP-адресу;
*  `-history n` - получение информации по последним n запросам, выведенной построчно;
*  `-help`- вывод информации о списке доступных пользователю команд;
*  `-exit` - завершение работы программы.
5) Все запросы в программе реализуются с помощью конструкции try...except.

## Формат вывода информации о погоде (пример)

Текущее время: 2023-10-03 09:48:47+03:00  
Название города: Санкт-Петербург  
Погодные условия: облачно  
Текущая температура: 12 градусов по цельсию  
Ощущается как: 11 градусов по цельсию  
Скорость ветра: 5 м/c  

## Установка программы
1) Установить интерпретатор python версии 3.11 (или выше)
2) Загрузить все файлы программы
3) Создать виртуальное окружение, установить туда все необходимые для работы программы библиотеки командой  `pip install -r requirements.txt`
4) Для запуска приложения ввести команду  `python main.py` в консоли из папки, в которой находится файл main.py