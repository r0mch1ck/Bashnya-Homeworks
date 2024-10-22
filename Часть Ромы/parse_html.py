import requests
from bs4 import BeautifulSoup

# URL страницы Википедии
url = 'https://ru.wikipedia.org/wiki/Московский_государственный_технический_университет_имени_Н._Э._Баумана'

# Выполнение GET запроса
response = requests.get(url)

# Проверка статуса запроса
if response.status_code == 200:
    # Парсинг HTML-кода страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Пример извлечения всех заголовков (например, h2 и h3)
    headers = soup.find_all(['h2', 'h3'])

    # Выводим все заголовки
    for idx, header in enumerate(headers, start=1):
        # Извлекаем текст заголовка
        header_text = header.text.strip()

        # Убираем ненужные символы вроде [править | править код]
        clean_text = header_text.replace("[править | править код]", "").strip()

        print(f"{idx}. {clean_text}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
