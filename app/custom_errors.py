from http import HTTPStatus


ERRORS_HTTP = {
    HTTPStatus.NOT_FOUND: "Город с таким названием не найден",
    HTTPStatus.BAD_REQUEST: "Проблемы с входными данными",
    HTTPStatus.UNAUTHORIZED: "Проблемы с авторизацией",
    HTTPStatus.FORBIDDEN: "Запрос отклонен сервером",
    HTTPStatus.REQUEST_TIMEOUT: "Плохое соединение"
}


class MyError(Exception):
    def __init__(self, msg=""):
        self.message = msg


class BadArgs(MyError):
    def __init__(self):
        super().__init__("Плохо заданы аргументы")


class UnknownCommand(MyError):
    def __init__(self):
        super().__init__("Неизвестная функция")


class FileNotFound(MyError):
    def __init__(self):
        super().__init__("Файл с историей не обнаружен")


class FailedToOpenFile(MyError):
    def __init__(self):
        super().__init__("Не удалось открыть файл")


class HTTPError(MyError):
    def __init__(self, code):
        self.message = ERRORS_HTTP.get(code, "Неудачная попытка запроса")
