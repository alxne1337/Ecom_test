NSFW Content Moderation API  

Это простое backend-приложение, написанное на Python с использованием FastAPI, которое принимает изображение через POST-запрос и проверяет его на наличие нежелательного (NSFW) контента с помощью бесплатного сервиса DeepAI NSFW API.

## ВАЖНО
Тестировал разные ссылки и способы, спросил у самого deepAI, ничего нельзя поделать, по реквесту на предложенную ссылку присылается ответ "This distribution is not configured to allow the HTTP request method that was used for this request. The distribution supports only cachable requests.\nWe can't connect to the server for this app or website at this time. There might be too much traffic or a configuration error."  
Если использовать предложенную самой нейросетью https://api.deepai.org/api/nsfw-detector ловится "Out of API credits - please enter payment info in your dashboard: https://deepai.org/dashboard\"

## Установка и запуск
    - Требования
        - Python 3.7+
        - pip
    - Шаги установки
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
