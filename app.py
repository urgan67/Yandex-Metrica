import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
import os

oauth_token = os.getenv('OAUTH_TOKEN')
counter_id = os.getenv('COUNTER_ID')



# Определение текущей даты
current_date = datetime.now().strftime('%Y-%m-%d')

# URL для запроса данных
api_url = 'https://api-metrika.yandex.net/stat/v1/data'

# Заголовки запроса
headers = {
    'Authorization': f'OAuth {oauth_token}'
}

# Функция для выполнения запроса и получения данных
def fetch_data(params):
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Ошибка запроса: {response.status_code}')
        print(response.text)
        return None

# Параметры запроса для получения общих метрик
general_params = {
    'ids': counter_id,
    'metrics': 'ym:s:users,ym:s:avgVisitDurationSeconds,ym:s:pageDepth,ym:s:bounceRate',
    'date1': current_date,
    'date2': current_date,
    'limit': 100
}

# Параметры запроса для получения поисковых запросов
search_params = {
    'ids': counter_id,
    'metrics': 'ym:s:visits',
    'dimensions': 'ym:s:searchPhrase',
    'date1': current_date,
    'date2': current_date,
    'limit': 10  # Количество результатов в отчете
}

# Получение и вывод основных метрик
general_data = fetch_data(general_params)
if general_data:
    print(f"Дата: {current_date}")
    print(f"Уникальные посетители: {general_data['totals'][0]}")
    print(f"Среднее время на сайте: {general_data['totals'][1]} сек")
    print(f"Глубина просмотра: {general_data['totals'][2]}")
    print(f"Количество отказов: {general_data['totals'][3]}%")
else:
    print("Данные по общим метрикам не получены")

# Получение и вывод поисковых запросов
search_data = fetch_data(search_params)
if search_data:
    print("Поисковые запросы:")
    for record in search_data['data']:
        search_phrase = record['dimensions'][0]['name'] if record['dimensions'] else 'Неизвестно'
        visits = int(record['metrics'][0])
        print(f"- {search_phrase}: {visits} визитов")
else:
    print("Данные по поисковым запросам не получены")