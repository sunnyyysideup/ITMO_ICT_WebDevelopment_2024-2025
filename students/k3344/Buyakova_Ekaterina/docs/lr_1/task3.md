# Задание 3

## Условие

Реализовать серверную часть приложения. Клиент подключается к серверу, и в ответ получает HTTP-сообщение, содержащее HTML-страницу, которая сервер подгружает из файла index.html.

### Требования:

- Обязательно использовать библиотеку socket.

## Реализация

Для выполнения задания был реализован сервер на основе библиотеки `socket`, который работает по протоколу TCP. Сервер загружает HTML-контент из файла `index.html` и отправляет его клиенту в формате HTTP-ответа.

## Пояснения к коду

### Серверная часть:

1. **Загрузка HTML-файла:** Сервер загружает содержимое файла `index.html` с помощью функции `load_html`. Если файл не найден, сервер возвращает сообщение об ошибке 404.

2. **Создание и настройка сокета:** Сервер создает TCP-сокет и привязывает его к локальному адресу и порту `8080`. Далее сокет переводится в режим ожидания входящих соединений с помощью метода `listen()`.

3. **Обработка запросов от клиентов:** Когда клиент подключается, сервер принимает соединение и получает HTTP-запрос клиента. Этот запрос может быть простой строкой, но в текущей реализации сервер игнорирует содержимое запроса и отправляет HTML-страницу в любом случае.

4. **Отправка HTTP-ответа:** Сервер формирует HTTP-ответ, включающий заголовки и содержимое HTML-страницы. Заголовки содержат информацию о типе контента (HTML) и его длине. Затем ответ отправляется клиенту, и соединение закрывается.

### HTML-страница `index.html`:

Сервер загружает HTML-страницу из файла index.html. Эта страница содержит простой HTML-документ с заголовком и текстом в теле.

## Тестирование

### Команда для запуска сервера: 
```bash
python server.py
```

## Результат

Когда клиент подключается к серверу, сервер отвечает HTTP-сообщением, содержащим HTML-контент. Если файл index.html существует, клиент получает содержимое этого файла. Если файл отсутствует, сервер возвращает сообщение с ошибкой 404.