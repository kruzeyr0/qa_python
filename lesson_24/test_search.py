import pytest
import logging

logging.basicConfig(    # Налаштування логування для запису інформації про запити та відповіді під час виконання тестів
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test_search.log"),
        logging.StreamHandler()
    ],
    force=True  # логуємо форс, щоб райтест не блочивив логування
)


test_data = [   # Різні комбінації параметрів сортування та обмеження для тестування пошуку автомобілів
    ("price", 5),
    ("price", 10),
    ("price", 15),
    ("year", 1),
    ("year", 5),
    (None, 1),
    ("engine_volume", 2),
]


@pytest.mark.parametrize("sort_by, limit", test_data)  # Параметризація тесту для перевірки різних комбінацій параметрів сортування та обмеження
def test_search_cars(auth_client, sort_by, limit):
    logging.info(f"Request: sort_by={sort_by}, limit={limit}")  # Логування параметрів запиту
    response = auth_client.get_cars(sort_by=sort_by, limit=limit)  # Викликаємо метод get_cars з параметрами сортування та обмеження

    assert response.status_code == 200
    data = response.json()  # Отримуємо список автомобілів у форматі JSON
    logging.info(f"Response: {data}")  # Логування відповіді
    assert isinstance(data, list)  # Перевіряємо, що відповідь є списком

    if sort_by == "price":  # Якщо параметр сортування - "price", перевіряємо, що автомобілі відсортовані за ціною
        prices = [car["price"] for car in data]
        assert prices == sorted(prices)

    if limit:
        assert len(data) <= limit  # Перевіряємо, що кількість отриманих автомобілів не перевищує вказане обмеження


