import requests

base_url = "http://127.0.0.1:5000"
upload_url = f"{base_url}/upload"
image_url = f"{base_url}/image/"
delete_url = f"{base_url}/delete/"

headers = {
    "Content-Type": "text"
}

test_image = {
    "image": open("photo_1.jpg", "rb") # відкриваємо зображення 
}

# POST:

upload_response = requests.post(upload_url, files=test_image) # надсилаємо POST-запит на завантаження зображення
post_data = upload_response.json() # отримуємо дані про завантажене зображення
#print(upload_response.json()) # тестовий вивід даних про завантажене зображення для перевірки


test_image_url = post_data.get("image_url", headers) # отримуємо URL завантаженого зображення
print(f"Uploaded image URL: {test_image_url}") # виводимо URL завантаженого зображення для перевірки

if upload_response.status_code == 201: # перевіряємо, чи запит був успішним
    print("Image uploaded successfully.")
else:
    print("Failed to upload image.")

test_image["image"].close() # закриваємо файл після завантаження

# GET:

filename = test_image_url.split("/")[-1] # отримуємо ім'я файлу з URL
image_file_url = f"{image_url}{filename}"

response = requests.get(image_file_url)

print(f"Response status code: {response.status_code}") # перевіряємо статус-код та відповідь сервера
print(f"Response JSON: {response.json()}")

# DELETE:

delete_response = requests.delete(f"{delete_url}{filename}") # надсилаємо DELETE-запит для видалення зображення

print(f"Delete response status code: {delete_response.status_code}") # перевіряємо статус-код та відповідь сервера
print(f"Delete response JSON: {delete_response.json()}")

