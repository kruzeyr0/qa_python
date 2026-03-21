import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"

search_params = {
  "q": "Curiosity rover Mars", # пошуковий запит
  "media_type": "image", # тільки зображення
  "page_size": 20 # щоб було з чого вибрати
}
  
# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"
###########################################################################################

response = requests.get(search_url, params=search_params)
response.raise_for_status() 
get_data = response.json()

#print(get_data["collection"]["items"][0]["data"][0]["nasa_id"]) # тестовий вивід першого nasa_id для перевірки

nasa_ids = [] # список для збереження nasa_id з результатів пошуку

items = get_data.get("collection", {}).get("items", [])[:2] # беремо з респонса дати айтемів, якщо вони є і обмежуємо до перших 2 по завданню

for item in items:
    nasa_id = item.get("data", [{}])[0].get("nasa_id") # отримуємо nasa_id з кожного айтема

    nasa_ids.append(nasa_id) # додаємо nasa_id до списку

#print(nasa_ids) # тестовий вивід списку nasa_id для перевірки

image_urls = [] # список для збереження URL зображень

for nasa_id in nasa_ids:
    asset_url = asset_url_template.format(nasa_id=nasa_id) # формуємо URL для отримання файлів по nasa_id

    asset_url_response = requests.get(asset_url) # робимо запит до сформованого URL
    
    asset_data = asset_url_response.json() # отримуємо JSON відповідь

    jpg_files = asset_data.get("collection", {}).get("items", []) # отримуємо список файлів з відповіді

    for file in jpg_files:
        href = file.get("href") # отримуємо URL файлу

        if href and href.endswith(".jpg"): # перевіряємо, чи URL існує і чи закінчується на .jpg
            image_urls.append(href) # додаємо URL зображення до списку
            break # припиняємо пошук після першого знайденого .jpg файлу для цього nasa_id


#print(image_urls) # тестовий вивід списку URL зображень для перевірки

first_image = requests.get(image_urls[0]) # робимо запит до першого URL зображення
open("photo_1.jpg", "wb").write(first_image.content) # зберігаємо зображення у файл

second_image = requests.get(image_urls[1]) # повторюємо для другого
open("photo_2.jpg", "wb").write(second_image.content) 