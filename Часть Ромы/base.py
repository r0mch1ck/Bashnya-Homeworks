import requests
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Api ключ
api_key = os.getenv("OPENWEATHER_API_KEY")

# Базовый URL для API запроса погоды
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Название города для запроса погоды
city_name = "Москва"

# Формирование полного URL для запроса
url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"

# Заголовки запроса
headers = {
    "Accept": "application/json",
    "User-Agent": "Weather API Client 1.0"
}

# Задание тайм-аута (например, 10 секунд)
timeout = 10

try:
    # Выполнение GET запроса с указанием тайм-аута
    response = requests.get(url, headers=headers, timeout=timeout)

    # Проверка статуса ответа
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"The weather in {city_name} is {temperature}°C with {description}.")
    else:
        print(f"Failed to retrieve weather data for {city_name}. Status code: {response.status_code}")
except requests.exceptions.Timeout:
    print(f"Request to OpenWeather API timed out after {timeout} seconds.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
