NSFW Content Moderation API

Это простое backend-приложение, написанное на Python с использованием FastAPI, которое принимает изображение через POST-запрос и проверяет его на наличие нежелательного (NSFW) контента с помощью бесплатного сервиса DeepAI NSFW API.

## Установка и запуск
Требования
    - Python 3.7+
    - pip
Шаги установки
    - Клонируйте репозиторий:
        - "git clone [<Ссылка на репозиторий>](https://github.com/alxne1337/Ecom_test)"
        - "cd Ecom_test"
    - Установите необходимые зависимости:
        - "pip install -r requirements.txt"
    - Создайте файл .env в корне проекта и добавьте ваш API-ключ DeepAI:
        - "API_KEY=ваш_ключ_от_DeepAI"
    - Запустите сервер:
        - "uvicorn main:app --reload"

## Использование
    - Через Postman:
        - метод POST
        - URL: http://localhost:8000/nsfw-check
        - В разделе "Body" выбрать "form-data"
        - Добавить ключ: file, тип: File, выбрать изображение (.jpg, .png)

## Ответы API
    Если изображение безопасное: {"status": "OK"}
    Если изображение содержит неприемлемый контент (nsfw_score > 0.7): {"status": "REJECTED", "reason": "NSFW content"}