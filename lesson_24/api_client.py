import requests
import config
from requests.auth import HTTPBasicAuth


class APIClient:    # APIClient клас для взаємодії з API

    def __init__(self): # ініціалізація базового URL та сесії для запитів

        self.base_url = config.BASE_URL
        self.auth = config.AUTH_ENDPOINT
        self.session = requests.Session()
    
    def authenticate(self, username, password):
        url = f"{self.base_url}{self.auth}"   # Формуємо URL для аутентифікації

        response = self.session.post(url, auth=HTTPBasicAuth(username, password))   # Відправляємо POST запит для аутентифікації користувача
    
        assert response.status_code == 200
        token = response.json()["access_token"]   # Отримуємо токен з відповіді
        assert token is not None
        
        self.session.headers.update({"Authorization": f"Bearer {token}"})   # Додаємо токен до заголовків сесії для подальших запитів
    
    def get_cars(self, sort_by=None, limit=None):   # Метод для отримання списку автомобілів
        url = f"{self.base_url}{config.CARS_ENDPOINT}"   # Формуємо URL для отримання автомобілів

        params = {}

        if sort_by: 
            params["sort_by"] = sort_by   # Додаємо параметр сортування до запиту, якщо він вказаний
        
        if limit:
            params["limit"] = limit   # Додаємо параметр обмеження кількості результатів до запиту, якщо він вказаний

        response = self.session.get(url, params=params)   # Відправляємо GET запит для отримання автомобілів
        return response   # Повертаємо список автомобілів у форматі JSON

