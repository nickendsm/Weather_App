from http import HTTPStatus

ERRORS_HTTP = {
    HTTPStatus.NOT_FOUND: "Город с таким названием не найден",
    HTTPStatus.BAD_REQUEST: "Проблемы с входными данными",
    HTTPStatus.UNAUTHORIZED: "Проблемы с авторизацией",
    HTTPStatus.FORBIDDEN: "Запрос отклонен сервером",
    HTTPStatus.REQUEST_TIMEOUT: "Плохое соединение"
}
