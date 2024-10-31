# Задание 5

## Условие

Написать простой веб-сервер для обработки GET и POST HTTP-запросов с помощью библиотеки socket в Python.

## Задание

Серевер должен:

1. Принять и записать информацию о дисциплине и оценке по дисциплине.
2. Отдать информацию обо всех оценках по дисциплинам в виде HTML-страницы.

## Реализация

Сервер использует библиотеку socket для обработки HTTP-запросов и отвечает на запросы с методами GET и POST. 

### Серверная часть:

Серверная часть реализована с использованием библиотеки `socket` для работы с TCP-соединениями и HTTP-запросами:

1. **GET-запросы**:
   - При получении GET-запроса сервер возвращает HTML-страницу с таблицей, содержащей дисциплины и оценки.
   - В таблице отображаются все дисциплины, добавленные ранее через POST-запросы, а также форма для добавления новых данных.

2. **POST-запросы**:
   - При получении POST-запроса сервер извлекает данные, переданные в теле запроса (дисциплина и оценка).
   - Эти данные сохраняются в список `grades`, который хранит все добавленные дисциплины и их оценки.
   - После обработки POST-запроса сервер перенаправляет пользователя обратно на главную страницу с таблицей.

3. **Обработка запросов**:
   - Сервер использует функцию `handler` для обработки каждого подключения клиента. В зависимости от типа запроса (GET или POST) вызывается соответствующая функция.
   - POST-запросы обрабатываются в функции `handle_post`, где данные запроса парсятся, и в список `grades` добавляется новая дисциплина с оценками.
   - GET-запросы обрабатываются в функции `handle_get`, которая генерирует HTML-страницу с текущими данными.

4. **Параллельная обработка запросов**:
   - Для обработки нескольких подключений одновременно используется библиотека `threading`. Для каждого запроса создается новый поток, чтобы сервер мог обрабатывать несколько запросов без задержек.

### Команда для запуска сервера: 
```bash
python server.py
```

## Результат

При помощи библиотеки socket веб-сервер обрабатывает GET- и POST-запрсы. Через POST-запрос можно отправить информацию о дисциплине и оценках, а через GET-запрос получить HTML-страницу с таблицей всех добавленных данных.