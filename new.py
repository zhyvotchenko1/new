import requests
import json
import re


def search_phone_numbers(api_key, cx, site_url):
    try:
        # Формируем запрос к Google Custom Search JSON API
        search_url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q=site:{site_url}"

        # Отправляем запрос и получаем результаты
        response = requests.get(search_url)
        if response.status_code == 200:
            data = response.json()

            # Извлекаем результаты из JSON-ответа
            if 'items' in data:
                phone_numbers = []
                for item in data['items']:
                    # Извлекаем текст из результатов поиска
                    snippet = item.get('snippet', '')

                    # Используем регулярное выражение для поиска номеров телефонов
                    numbers = re.findall(r'\b8\d{10}\b', snippet)
                    phone_numbers.extend(numbers)

                return phone_numbers
            else:
                print("Результаты поиска не найдены.")
                return []
        else:
            print(f"Ошибка при выполнении запроса: {response.status_code}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


if __name__ == "__main__":
    # Введите свой API-ключ и Custom Search Engine ID (cx)
    api_key = 'YOUR_API_KEY'
    cx = 'YOUR_CX'
    site_url = 'hands.ru/company/about'  # URL-адрес веб-страницы для поиска номеров телефонов

    phone_numbers = search_phone_numbers(api_key, cx, site_url)
    if phone_numbers:
        print("Найдены следующие номера телефонов:")
        for phone_number in phone_numbers:
            print(phone_number)
    else:
        print("На данной странице номера телефонов не найдены.")
