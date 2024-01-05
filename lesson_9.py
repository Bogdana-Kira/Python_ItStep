import requests
from bs4 import BeautifulSoup
url = "https://auto.ria.com/uk/"  # Замініть на URL-адресу веб-сайту, яку ви хочете витягти

response = requests.get(url) # Надіслати запит GET на URL-адресу

# Перевірте, чи був успішний запит (код статусу 200)
if response.status_code == 200:
    # Розбір HTML-змісту сторінки за допомогою BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Знайти всі заголовки (можливо, вам потрібно оглянути HTML для отримання правильного тегу)
    headers = soup.find_all(["h1", "h2", "h3"])  # Відредагуйте за потребою

    # Вивести текст кожного заголовка
    for header in headers:
        print(header.text)

else:
    print(f"Не вдалося отримати сторінку. Код статусу: {response.status_code}")
