# REST API для Anyera Digital & Design.

[Тестовое задание](https://docs.google.com/document/d/1OSgG7qUW1Rm_5VEc5BEZqSnJHa-_10AvA1vnmU2RBZE/edit?usp=sharing)

**_Данный сервис развернут на сервере по адресу: [Документация AnyeraProject](http://5.104.108.168:8009/swagger/)_**

## Установка

Перед началом установки убедитесь, что у вас установлен Python 3.11 и Poetry (пакетный менеджер для Python).

1. Склонируйте репозиторий:

`git clone https://github.com/192117/AnyeraProject.git`

2. Перейдите в директорию:

`cd AnyeraProject`

## Запуск приложения без Docker Compose (после пункта "Установка")

1. Установите зависимости с помощью Poetry:

`poetry install`

2. Создайте переменные окружения:

_Создайте файл .env на основе .env.example для запуска без Docker и файл .env.docker на основе .env.docker.example для 
запуска с Docker. Оба файла содержат переменные окружения, которые требуются для настройки приложения._

3. Запустите приложеие с помощью Poetry:

`poetry run gunicorn -b 0.0.0.0:8000 AnyeraProject.wsgi:application`

4. Доступ к приложению: 

- [Документация swagger](http://127.0.0.1:8000/swagger/)
- [Документация redoc](http://127.0.0.1:8000/redoc/)

Работает без использования Nginx.

## Запуск приложения c использованием Docker Compose (после пункта "Установка")

1. Создайте переменные окружения:

_Создайте файл .env на основе .env.example для запуска без Docker и файл .env.docker на основе .env.docker.example для 
запуска с Docker. Оба файла содержат переменные окружения, которые требуются для настройки приложения._

2. Запустите сборку docker-compose:

`docker compose up -d --build`

3. Доступ к приложению: 

- [Документация swagger](http://127.0.0.1:8000/swagger/)
- [Документация redoc](http://127.0.0.1:8000/redoc/)

Работает с использованием Nginx.

## Schema OPEN API

[Схема](https://github.com/192117/AnyeraProject/blob/master/AnyeraProject.yaml)