from http import HTTPStatus


FILE_NOT_FOUND_MSG = "Файл с историей не обнаружен"
UNKNOWN_ERROR = "Неизвестная ошибка"
UNKNOWN_COMMAND_MSG = "Неизвестная функция"
FAILED_TO_OPEN_MSG = "Не удалось открыть файл"
FAIL_TO_PARSE_MSG = "Плохо заданы аргументы"


ERRORS_HTTP = {
    HTTPStatus.NOT_FOUND : "Город с таким названием не найден",
    HTTPStatus.BAD_REQUEST : "Проблемы с входными данными",
    HTTPStatus.UNAUTHORIZED : "Проблемы с авторизацией",
    HTTPStatus.FORBIDDEN : "Запрос отклонен сервером",
    HTTPStatus.REQUEST_TIMEOUT : "Плохое соединение"
}
